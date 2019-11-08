# import module datatime
import datetime
# dari folder django lalu folder db(django.db) import module models
from django.db import models
# import timezone
from django.utils import timezone

# Perhatikan penambahan import datetime dan dari django.utils import timezone, 
# itu untuk referensi modul datetime standar Python dan utilitas terkait zona waktu Django di django.utils.timezone, masing-masing.

# Create your models here.
# model for question
# di parameter kita ekstend gitu lah ke class Model yang ada di module moles
# untuk memberi tau bahwa class Question ini adalah model
# ketika kita sudah menginisailisaikan app kepada project, lalu kita lakukan sqlmigrate polls_app 0001
# maka didabase kita akan dibuatkan tabel polls_app_question
class Question(models.Model):
    # python django akan menganggap ini sebuah variabel di dalam class Question, 
    # tetapi, di dabase variabel ini akan menjadi field di dalam tabel polls_app_question
    # di dalam module models memungkinkan kita menggunakan class yang class itu akan membuatkan kerangka untuk menciptakan sebuah tabel di database
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # menambahkan method __str__()
    # agar kita bisa merepresentasi kan object question_text dengan mudah dibaca isinya(humaneble)
    def __str__(self):
        return self.question_text
    # menambahkan method was_published_recently()
    # mengembalikan True ketika Question diterbitkan dalam hari terakhir
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # ### membetulkan bug: pub_date dari masa depan harusnya mengembalikan False bukan True.
    def was_published_recently(self):
        # attribut now menyimpan timezone saat ini(timezone.now())
        now = timezone.now()
        # kembalikan question_text dari __str__(self)
        # yang timezone-nya(waktunya) dari masa lalu,
        # masa sekarang(now) dikurang timedelta(days=1).
        # dan yang kurang dari atau sama dengan pub_date
        # atau kurang dari atau sama dengan now(waktu saat ini)
        # !!!ATTENTION!!! method ini akan me-return True jika question dibuat pada 24jam terkhir.
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    # dengan ini header/nama column bisa diklik dan ketika di klik akan menyortir berdasarkan 'pub_date'
    was_published_recently.admin_order_field = 'pub_date'
    # ini akan mengganti isi field dari column Published recently?
    # menjadi True(django defaultnya ketika True akan metampilkan dalam bentuk icon)
    was_published_recently.boolean = True
    # ini akan mengganti nama column-nya, defaul adalah nama yang dimasukan pada admin.QuestionAdmin pada tuple list_display.
    was_published_recently.short_description = 'Published recently?'

# model for Choice
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # menambahkan method __str__()
    # agar kita bisa merepresentasi kan object question_text dengan mudah dibaca isinya(humaneble)
    def __str__(self):
        return self.choice_text
    