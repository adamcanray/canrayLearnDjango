# dari modul django.http import Http404
# from django.http import Http404
# dari module django.template import loader
# from django.template import loader

# source: https://docs.djangoproject.com/en/2.2/intro/tutorial01/
from django.http import HttpResponseRedirect
# import render() dari modul shortcuts
from django.shortcuts import get_object_or_404, render
# dari modul django.urls import reverse
from django.urls import reverse
# dari django.views import func generic
from django.views import generic

# dari modul .models import class Question
from .models import Question, Choice

# dari modul dajngo.utils import method timezone
from django.utils import timezone

# race confition using F()
from django.db.models import F

# index TIDAK MENGGUNAKAN generic views
# views untuk index
# def index(request):
#     # list untuk menyimpan pertanyaan terkhir
#     # variabel ini berisi query langsung ke models Question
#     # lalu mengambil data pub_date terbaru menggunakan '-'
#     # dan ambil dari yang index ke-0 sampai ke-5
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
#     # output berisi perulangan pada field question_text sebanya latest_question_list
#     # dan ', ' sebagai sparator sertiap akhir perulangan.
#     # output = ', '.join([q.question_text for q in latest_question_list])
    
#     # variabel template berisi loader untuk mengambil template pada folder template/polls_app/index.html
#     # template = loader.get_template('polls_app/index.html')

#     # context
#     context = {'latest_question_list' : latest_question_list,}

#     # kembalikan nilai output
#     # return HttpResponse(output)

#     # kembalikan template dan render request, urls yang mengarah pada template kita dan context(berisi data dari database)
#     return render(request, 'polls_app/index.html', context)
# index MENGGUNAKAN generic views
# index views
# class IndexView Ekstends ke generic.ListView
class IndexView(generic.ListView):
    # isi attribut template_name(bawaan generic view)
    template_name = 'polls_app/index.html'
    # isi attribut context_object_name(bawaan generic view)
    # menyimpan object, yaitu data hasil dari model(query langsung ke database)
    # pada response dipanggil dengan context['lates_question_list']
    context_object_name = 'latest_question_list'
    # func get_queryset(self) - untuk me-request dengan query langsung dari model Question
    def get_queryset(self):
        """mengembalikan lima buah question terbaru yang di publish"""
        return Question.objects.filter(
            # pub_date__lte - __lte artinya less than od equal
            # jadi filter berdasarkan pub_date yang kurang dari atau sama dengan timezone.now()
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

# detail TIDAK MENGGUNAKAN generic views
# views untuk detail
# def detail(request, question_id):
#     # # jika id yang dimasukan pada url itu sama dengan question_id pada database 
#     # try:
#     #     # maka, dari class Question ambil primary_key=question_id
#     #     # dan simpan ke variabel question
#     #     question = Question.objects.get(pk=question_id)
#     # # jika id di url tidak sesuai dengan yang ada di database(DoesNotExist/tidak tersedia)
#     # except Question.DoesNotExist:
#     #     # maka tampilan pesan kesalahan pada Page Not Found 404
#     #     raise Http404("Question does not exist")
#     # cara diatas bisa dipermudah dengan shortcut: get_object_or_404()
#     # var question berisi, perintah get_object_or_404(namaModel, dataApaYgInginDiAmbil)
#     # dengan ini saja fungsi nya sudah seperti menggunakan try dan except
#     # jika data id di url sesuai dengan field question_id pada database, maka tampilkan
#     # jika tidak maka tampilkan pesan kesalahan 404
#     question = get_object_or_404(Question, pk=question_id)
#     # jika tanpa shortcut render() - harus menggunakan HttpResponse
#     # return HttpResponse("You're looking at question %s." % question_id)
#     # kembalikan nilai dengan merender template
#     # render() pengganti HttpResponse
#     # pada render(req_method, halaman template, kiridata object pada halaman tersebut)
#     return render(request, 'polls_app/detail.html', {'question':question})
# detail MENGGUNAKAN generic views
# class DetailView Ekstends ke generic.DetailView
# halaman yang membutuhkan id spesific, maka ekstends ke DetailView
class DetailView(generic.DetailView):
    # isi attribut model
    model = Question
    # isi attribut template_name
    template_name = 'polls_app/detail.html'
    # method untuk tidak menampilkan question yang tidak pernah dipublikasikan(dari masa depan)
    def get_queryset(self):
        """
        Tidak termasuk pertanyaan apa pun yang belum dipublikasikan/jika pertanyaan belum pernah dipublikasikan jangan kasih akses untuk detail view.
        """
        # mengembalikan hasil dari model Quetion dengan filter(hanya question yang pub_date-nya less thanor equal timezone.now())
        return Question.objects.filter(pub_date__lte=timezone.now())


# results TIDAK MENGGUNAKAN generic views
# views untuk result
# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)

#     # buat variabel question
#     question = get_object_or_404(Question, pk=question_id)
#     # kembalikan nilai dengan merender template
#     return render(request, 'polls_app/results.html', {'question' : question})
# results MENGGUNAKAN generic views
# class ResultsView Ekstends ke generic.DetailView
class ResultsView(generic.DetailView):
    # isi attribut model
    model = Question
    # isi attribut template_name
    template_name = 'polls_app/results.html'
    # method untuk tidak menampilkan question yang tidak pernah dipublikasikan(dari masa depan)
    def get_queryset(self):
        """
        Tidak termasuk pertanyaan apa pun yang belum dipublikasikan/jika pertanyaan belum pernah dipublikasikan jangan kasih akses untuk detail view.
        """
        # mengembalikan hasil dari model Quetion dengan filter(hanya question yang pub_date-nya less thanor equal timezone.now())
        return Question.objects.filter(pub_date__lte=timezone.now())

# views proses untuk hasil vote, dan akan ditampilkan pada result
def vote(request, question_id):
    # dumnmy ipmolementation / implementasi buatan
    # return HttpResponse("You're voting on question %s." % question_id)

    # buat variabel question, dimana akan memanggil helper function get_object_or_404
    # dan memberi argument Quesetion, pk=quesetion_id
    question = get_object_or_404(Question, pk=question_id)
    try:
        # jika ada radio button yangter-select maka simpan id yang terdapat pada value di tag input form HTML
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # jika KeyError atau choice tidak tersedia(form choice tidak diisi)
    except (KeyError, Choice.DoesNotExist):
        # tampiklan ulang question voting form dengan mengirimkan error message
        return render(request, 'polls_app/detail.html', {
        'question' : question,
        'error_message' : "You didn't select a choice."
    }) 
    else:
        # votes ditambah 1
        # belajar mencoba menggunakan function f()
        # untuk menghindari race condition makadari itu menggunakan F()
        selected_choice.votes = F('votes') + 1
        # lalus save()
        selected_choice.save()
        # selalu return HttpResponseRedierect setelah sukses berurusan
        # dengan POST data. ini mencegah data terkirim dua kali
        # jika ada user yang menekan tombol kembali.
        # mengirim data ke views results
        return HttpResponseRedirect(reverse('polls_app:results', args=(question.id,)))
        # hasil dari reverse() adalah string /polls_app/3/result/