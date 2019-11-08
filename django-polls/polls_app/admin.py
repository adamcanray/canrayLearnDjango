from django.contrib import admin

# Register your models here.

# dari modul models.py yang ada di folder yang sama, dan import class Question
from .models import Question, Choice

# TAMPILAN FIELD DEFAULT
# daftarkan model Question ke admin site
# admin.site.register(Question)

# buat class untuk membuat model Choice menjadi inline
# class ChoiceInline(admin.StackedInline):
# menggunakan TabularInline
class ChoiceInline(admin.TabularInline):
    # model yang digunakan pada class ini
    model = Choice
    # ingin menampilkan berapa banyak field choices pada tampilan question site admin nanti-nya
    extra = 3

# kustom field folmulir pada admin site Question(ketika membuat question baru pada halaman admin) 
class QuestionAdmin(admin.ModelAdmin):
    # urutan field nya(pub_date terlebih dahulu baru questoin_text)
    # fields = ['pub_date', 'question_text']
    # fieldsets untuk membuat beberapa bidang
    fieldsets = [
        # bidang pertama
        # index pertama adalah text dari template title bar yang disediakan django,
        # jika tidak ingin menggunakan title bar isi saja index pertama dengan None.
        # index kedua dari tuple adalah pasangan key(fields) dan value(question_text).
        (None, {'fields' : ['question_text']}),
        # bidang kedua
        # index pertama adalah text dari template title bar yang disediakan django,
        # jika tidak ingin menggunakan title bar isi saja index pertama dengan None.
        # index kedua dari tuple adalah pasangan antara key dan value.
        # ------ READ
        # pada index kedua object berisi dua pasangan key dan value
        # --- pertama adalah pub_date milik model Question dan
        # --- kedua adalah 'classes' yang berisi ['collapse'] : 
        # *----- pada kasus ini fild Date information diberi collapse, efeknya adalah:
        # *------------ pada bidang/field Date infomation akan dihide pada saat halaman direload(dan disediakan tombol 'show')
        ('Date information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
    ]
    # yang inline ke class QuestionAdmin adalah class ChoiceInline
    inlines = [ChoiceInline]
    # list display akan menampilkan berupa kolom baru('question_text' akan ditampilkan memnjadil QUESTION TEXT) beserta isi-nya(dari model)
    # pada question list page kolom-kolom ini bisa diklik untuk sort berdasarkan(ASC/DESC)
    # was_published_recently tidak bisa diklik karena Output dati method arbitrary(method buatan sendiri).
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # membuat sidebar default yang bisa di klik dan akan menyortir berdasarkan 'pub_date'
    list_filter = ['pub_date']
    # membuat search-box pada bagian atas di question lists page.
    search_fields = ['question_text']

# daftarkan model Quetiond engan custom folmulir untuk halaman admin site question.
# class custom folmulir admin jadikan argument kedua.
admin.site.register(Question, QuestionAdmin)

# hapus model Choice dari daftar admin/akan membuat Choice Inline/didalam Question.
# dalam kata lain nanti-nya choices bisa dilihat dan dimanipulasi dari tampilkan admin site Quetions.
# daftarkan model Choice
# admin.site.register(Choice)