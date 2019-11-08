# dari modul django.urls import function path
from django.urls import path
# dari directory yang sama, import modul views(views.py)
from . import views

# buat namespace 'polls_app'
# dengan mengisi attribut/variabel app_name(nama default/tidak boleh diganti)
# mungkin jika app nya banyak, bisa:
# app_name = 'polls_app_satu'
# app_name = 'polls_app_dua'
app_name = 'polls_app'

# pola url pada app polls_app
urlpatterns = [
    # # code tanpa generic view
    # # contoh: /polls/
    # path('', views.index, name='index'),
    # # custom url: menambahkan spesific
    # # path('spesifics/<int:question_id>/', views.detail, name='detail'),
    # # contoh: /polls/5/
    # # value 'name' dipanggil oleh {% url %} template tag
    # path('<int:question_id>/', views.detail, name='detail'),
    # # contoh: /polls/5/result/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # contoh: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    # code dengan generic view
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]