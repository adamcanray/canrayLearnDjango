# Belajar Django
Versi Python: **3.7.0**

Versi Django: **2.2.6**

Structure Files:
* Env/ </br>
  folder ini harus ada sebagai **virtualenv**. saya tidak meng-upload nya pada repo ini karena size yang lumayan hingga 109 MB(tergantung packages apasaja yang sudah terinstall). saya bisa membuat **virtualenv** dengan command berikut: ```python -m venv Env``` -- artinya kita ingin membuat sebuah **virtualenv** dengan nama folder-nya **Env**. pastikan virtual Env berada pada **main folder**.
* 0_catatan/
  * **0000_race_condition** -- cara mengatasi **race condition** pada django - Source: https://docs.djangoproject.com/en/2.2/ref/models/expressions/#f-expressions.
  * **tutorial_part_1.txt** -- catatan panjang perjalanan saya pada tutorial django part_1 - Source: https://docs.djangoproject.com/en/2.2/intro/tutorial01/
  * **tutorial_part_2.txt** -- catatan panjang perjalanan saya pada tutorial django part_2 - Source: https://docs.djangoproject.com/en/2.2/intro/tutorial02/
  * **tutorial_part_3.txt** -- catatan panjang perjalanan saya pada tutorial django part_3 - Source: https://docs.djangoproject.com/en/2.2/intro/tutorial03/
  * **tutorial_part_4.txt** -- catatan panjang perjalanan saya pada tutorial django part_4 - Source: https://docs.djangoproject.com/en/2.2/intro/tutorial04/
  * **tutorial_part_5.txt** -- catatan panjang perjalanan saya pada tutorial django part_5 - Source: https://docs.djangoproject.com/en/2.2/intro/tutorial05/
  * **tutorial_part_6.txt** -- catatan panjang perjalanan saya pada tutorial django part_6 - Source: https://docs.djangoproject.com/en/2.2/intro/tutorial06/
  * **tutorial_part_7.txt** -- catatan panjang perjalanan saya pada tutorial django part_7 - Source: https://docs.djangoproject.com/en/2.2/intro/tutorial07/
  * **reusable_apps.txt** -- bagaimana sebuah **apps** yang kita buat pada **project Django** itu bisa digunakan berkali-kali(**efisiensi**).
* mywebsite/
  * mywebsite/
    * **__pycache__**/ -- directory ini akan menyimpan **cache(.pyc)** dari beberapa file di dalam **project**.
    * **__init__.py** -- file ini adalah untuk menandakan/meng-inisialisasi bahwa ini adalah **project** dan ini secara default sudah tersedia ketika kita membuat sebuah **project Django**.
    * **settings.py** -- file isi berisi configurasi **BASE DIR**, **INSTALLED_APPS**, **DATABASES**, **TIME_ZONE**, dll.
    * **urls.py** -- ini adalah file untuk mengatur/mendaftarkan **apps Django** kepada **project Django** agar bisa diakses ketika **Web Server** dijalankan.
    * **wsgi.py** -- adalah file **config** untuk **Project**, kita men-setting default Project disini.
  * sqlite/
    * sqldiff.exe -- documentation: https://www.sqlite.org/docs.html
    * sqlite3_analyzer.exe -- documentation: https://www.sqlite.org/docs.html
    * sqlite3.exe -- untuk menjalankan **database command** pada Sqlite3. documentation: https://www.sqlite.org/docs.html
  * **db.sqlite3** -- ini adalah file database yang dibuat dengan **sqlite3**.
  * **manage.py** -- adalah **file kunci** yang untuk menjalankan **testing**, **runserver** dan semua yang kontrol ada di file ini. contoh penggunaan: ```python manage.py runserver```
  * **sqlite3.exe** ini adalah **execute** untuk membuka **database command** pada sqlite3.
* django-polls/ </br>
  ini adalah folder yang digunakan untuk mengubah **Django apps** menjadi sebuah **reusable app** yang efisien dalam penggunaannya dan membuat sebuah **Django apps** menjadi sebuah **packages** yang bisa di install pada **pip** dan bisa di-**Distribusikan** pada **Python Packages Index(PyPI)** agar bisa/mudah digunakan oleh developer/pengembang lain.
  * **dist/** -- folder berisi **Archives Packages** yang siap upload(ber-ekstensi **namaFolderMain-versionPadaSetup.tar.gz**). atau Archives apapun yang diperlukan untuk proses **packaging**.
  * **django_polls.egg-info/** -- adalah folder yang akan berisi file informasi setelah **proses Packaging(menjalankan setup.py)**
  * **docs/** -- folder ini berisi documentation(Optional) yang menambah penjelasan tentang **packages** yang saya buat.
  * **polls_app/** </br>
  ini adalah folder **apps Django** yang saya buat di dalam folder project **mywebsite/mywebsite/polls_app/**. dipindahkan kesini karena ini sudah melewati tahap **reusable apps** dan sudah di compact/compress ke **packages** agar bisa lebih efisien dan bisa digunakan siapa saja.
    * **__pycache__**/ -- directory ini akan menyimpan **cache(.pyc)** dari beberapa file di dalam **apps**.
    * **migration/**
      * **__pycache__**/ -- directory ini akan menyimpan **cache(.pyc)** dari beberapa file di dalam folder **migration/**.
      * **__init__.py** -- ini untuk meng-inisialisasikan folder **migration**.
      * **0001_initial.py** -- file ini terbuat ketika melakukan **migrasi/migration** pada **Models**.
    * **static/** </br>
    Folder ini untuk menyimpan **properti/assets** karena **Django** tahu bahwa untuk membuat sebuah aplikasi web yang bisa berinteraksi dengan pengguna aplikasi web tersebut butuh komponen tambahan untuk **Frond-end** seperti Image, CSS, Javascript, dll.
    * templates/ </br>
    Folder ini untuk menyimpan template-template dalam bentuk HTML yang memungkinkan saya untuk menampilkan data-data yang sudah di proses oleh **Models** ke halaman Website.
    * **__init__.py** -- ini untuk meng-inisialisasikan folder **polls_app** sebagai **apps**.
    * **admin.py** -- adalah file untuk memungkinkan saya meng-akses **admin site** dan juga memanupulasi tampilan-nyaagar tidak menggunakan tampilan/tataletak default.
    * **apps.py** -- adalah file untuk meng-configurasikan bahwa **'polls_app'** adalah **apps** dan nantinya file ini lah yang akan dimasukan pada list **INSTALLED_APPS** didalam file **mywebsite/settings.py**.
    * **models.py** -- ini adalah file untuk menulis **Model** saya yang berinteraksi langsung dengan **database**.
    * **tests.py** -- ini adalah file yang memungkinkan saya untuk **mengtest** method-method saya apakah mengembalikan nilai yang saya inginkan atau tidak. **tests** pada project Django atau project Python lain-nya itu sangat disarankan untuk pemeliharaan. saya bisa menjalankan file ini dengan: ```python manage.py test```.
    * **urls.py** -- file ini memungkinkan saya untuk mengatur **url** saya untuk dioprasikan pada website dan menentukan **views** apa yang akan saya tampilkan ketika pengguna menujur **url** tersebut.
    * **views.py** -- file ini mengatur **views** saya untuk ditampilkan pada **url tertentu**.
  * **LICENSE** -- adalah file yang memungkinkan saya memberikan LICENSE pada packages saya. untuk memberi informasi siapa saja yang berhak menggunakan **packages** saya.
  * **MANIFEST.in** -- adalah untuk menentukan apa-apa saja yang akan diikut sertakan dalam **packages** saya.
  * **README.rst** -- adalah sebuah penjelasan tentang **package** yang saya buat/bangun.
  * **setup.py** -- setup.py adalah file yang nantinya kita akan eksekusi untuk menghasilkan file Archives **.tar.gz** pada directory **dist/**. kita bisa eksekusi dengan mengetikan: ```python3 setup.py sdist``` arahkan pada directory yang terdapat **setup.py** dalam kasus saya ada di **django-polls/setup.py**. sebelum meng-eksekusi pastikan Python kamu sudah ter-install **setuptolls**. install: ```python3 -m pip install --user --upgrade setuptools```.