# !!!!!READ!!!!!
# tests dalam django sangat penting untuk menguji setiap kode yang kita buat.
# contoh:
# - kita membuat sebuah aplikasi poling, 
# - dan di view detail kita hanya ingin user hanya bisa melihat detail dari question yang tanggal publikasi-nya dari masalalu(past),
# - juga question yang tanggal publikasi-nya dari masa depan tidak akan ditampilkan pada index view.
# - tetapi ada celah. ketika user menebak/tahu sebuah id dari question tersebut(dari masa depan),
# - lalu user mengetik id pada url, contoh: /polls_app/3/
# - maka user akan tetap bisa melihat detail dari question yang seharusnya belum ditampilakan/dipublikasikan.
# solusi:
# - maka dari itu kita harus membuat sebuah tests, dimana tests ini bisa menyelesaikan masalah diatas,
# - dengan cara hanya menampilkan question yang pernah dipublikasikan(tanggalnya dari masalalu/past) pada halaman/view detail.
# - problem solve.
# !!!!!END!!!!!
 
# usahakan di dalam tests.py itu mengimport modul apapun sesuai dengan apa yang ini di test.
# daridjango.test import class TestCase
from django.test import TestCase
# import date time
import datetime
# dari django.utils import method timezone
from django.utils import timezone
# dari moduls model pada directori yang sama, import class/model Question
from .models import Question

# dari modul django.urls import reverse
from django.urls import reverse 

# TEST MODEL
# buat nama class apa saja bebas
# syaratnya hanya ekstend ke TestCase, contoh:
class QuestionModelTests(TestCase):
    # buat method untuk mengecek question yang dibuat pada tanggal masa depan.
    # karena system akan otomatis mencari apapun yang diawali dengan 'test' pada file tests.py ini,
    # maka kita definisikan method dengan nama yang awalannya test, contoh:
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() mengebalikan False untuk question yang
        pub_date nya itu berasal dari masa depan(tanggal masa depan).
        """
        # date dari masa 30 hari kedepan
        time = timezone.now() + datetime.timedelta(days=30)
        # menyimpan model yang attribut pub_date nya sudah dari masa depan
        future_question = Question(pub_date=time)
        # tampilkan kemungkinan yang benar atau yang seharusnya harus-nya
        # seharusnya adalah: jika pub_date dari masa depan maka False.
        self.assertIs(future_question.was_published_recently(), False)
    # buat method
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() return False untuk question yang pub_date-nya
        lebih lama dari satu hari
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
    # buat method
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() return True untuk question yang pub_date-nya
        waktunya dihari terkhir(hari sekarang/hari ini)
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

# TEST VIEW INDEX
# shorcut function
# menerimadua buah parameter berupa question_text dan days
def create_question(question_text, days):
    """
    Buat pertanyaan dengan `question_text` yang diberikan dan terbitkan
    diberikan jumlah offset `hari` ke sekarang (negatif untuk pertanyaan yang dipublikasikan
    di masa lalu, positif untuk pertanyaan yang belum dipublikasikan).
    """
    # attribut time = waktu sekarang + waktu dimana question dibuat
    time = timezone.now() + datetime.timedelta(days=days)
    # kembalikan hasil
    return Question.objects.create(question_text=question_text, pub_date=time)
# class ini untuk menge-tests views Index, ekstends ke TestCase
class QuestionIndexViewTests(TestCase):
    # method ketika tidak ada question
    def test_no_question(self):
        """
        Jika tidak ada pertanyaan, pesan yang sesuai akan ditampilkan.
        """
        # attribut response = get ke namespace url 'polls_app' dan name url-nya 'index', ada pada urls.py
        response = self.client.get(reverse('polls_app:index'))
        # jika question ada/tersedia, status_code-nya 200(OK)
        self.assertEqual(response.status_code, 200)
        # jika question tidak tersedia. tampilkan pesan error-nya, bahwa tidak ada question.
        self.assertContains(response, "No polls are available.")
        # dari url polls_app ambil context, lalu isi dengan array kosong
        # latest_question_list ini mengacu pada views index juga template index.html
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    # method untuk test_past_question
    def test_past_question(self):
        """
        question dengan pub_date dari masalalu(past) akan ditampilkan pada index page.
        """
        # jalankan shortcut method dengan memberi argument, minus(-) untuk masa lalu
        create_question(question_text="Past question.", days=-30)
        # attribut response mengambil data ke url view index
        response = self.client.get(reverse('polls_app:index'))
        # set Query untuk menampilkan data latest_question_list
        # latest_question_list ini mengacu pada views index juga template index.html
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            # data tidak dikosongkan
            ['<Question: Past question.>']
        )
    # method untuk test_future_question
    def test_future_question(self):
        """
        question dengan pub_date dari masa depan(future) tidak akan ditampilkan pada index page.
        """
        # jalankan method shortcut dengan memberi argument, days=angka positif berarti dari masa depan
        create_question(question_text="Future question.", days=30)
        # attribut response get ke url view index
        response = self.client.get(reverse('polls_app:index'))
        # pesan ketika tidak ada polls yang tersedia(karena ini tanggalnya dari masa depan)
        self.assertContains(response, "No polls are available.")
        # maka latest_question_list akan diisi array kosong
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    # method untuk test future question dan past
    def test_future_question_and_past_question(self):
        """
        bahkan ketika keduanya past(masalalu) dan future(masadepan) tersedia, hanya past question yang akan dtampilkan.
        """
        # jalankan method shortcut dengan memberi argument dengan asumsi question dari masalalu
        create_question(question_text="Past question.", days=-30)
        # jalankan method shortcut dengan memberi argument dengan asumsi question dari masa depan
        create_question(question_text="Future question.", days=30)
        # isi attribut response dengan data yang di get langsung ke url view index
        response = self.client.get(reverse('polls_app:index'))
        # set query agar hanya mengisi latest_question_list dengan Past Question.
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )
    # method untuk mengetest jika latest_qustion_list tersiri dari beberapa question
    def test_two_past_question(self):
        """
        Halaman indeks pertanyaan dapat menampilkan beberapa pertanyaan.
        """
        # jalankan method dengan memberi argument
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        # isi attribut response dengan data hasil get langsung ke url view index
        response = self.client.get(reverse('polls_app:index')) 
        # set query untuk mengisi latest_question_list dengan data hasil dari shorcut method
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            # harus yang days-nya lebih dekat ke masa sekarang/masa depan
            # karena jika terdekatke masa depan dipastikan itu yang terbaru tanggal/waktunya.
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

# TEST VIEW DETAIl
# 
class QuestionDetailViewTests(TestCase):
    # 
    def test_future_question(self):
        """
        detail view dari sebuah question dengan pub_date dari masa depan
        akan mengembalikan sebuah pesan 404 Not Found.
        """
        # 
        future_question = create_question(question_text="Future question.", days=5)
        # 
        url = reverse('polls_app:detail', args=(future_question.id,))
        # 
        response = self.client.get(url)
        # 
        self.assertEqual(response.status_code, 404)
    # 
    def test_past_question(self):
        """
        detail view dari sebuah question dengan pub_date dari masa lalu
        akan ditampilkan question_text-nya
        """
        # 
        past_question = create_question(question_text="Past question.", days=-5)
        # args -- mengirim argument pada parameter yang disediakan url yaitu id.
        url = reverse('polls_app:detail', args=(past_question.id,))
        # 
        response = self.client.get(url)
        # 
        self.assertContains(response, past_question.question_text)

# TEST VIEW RESULT
class QuestionResultsViewTests(TestCase):
    # 
    def test_future_question(self):
        """
        results view dari sebuah question dengan pub_date dari masa depan
        akan mengembalikan sebuah pesan 404 Not Found.
        """
        # 
        future_question = create_question(question_text="Future question.", days=5)
        # 
        url = reverse('polls_app:results', args=(future_question.id,))
        # 
        response = self.client.get(url)
        # 
        self.assertEqual(response.status_code, 404)
    # 
    def test_past_question(self):
        """
        results view dari sebuah question dengan pub_date dari masa lalu
        akan ditampilkan question_text-nya
        """
        # 
        past_question = create_question(question_text="Past question.", days=-5)
        # args -- mengirim argument pada parameter yang disediakan url yaitu id.
        url = reverse('polls_app:results', args=(past_question.id,))
        # 
        response = self.client.get(url)
        # 
        self.assertContains(response, past_question.question_text)