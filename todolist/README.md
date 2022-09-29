# Tugas 4 Pengimplementasian Form dan Autentikasi Menggunakan Django

[HerokuAPP](https://django-tugaspbp2raspati.herokuapp.com/todolist/)

# Kegunaan {% csrf_token %} pada elemen <form>

    Kepanjangan dari CSRF sendiri adalah Cross Site Request Forgery. Token ini berguna untuk keamanan user and site, jika user tidak memiliki token atau tokennya berbeda dengan yang ada server maka requestnya tidak akan di eksekusi. Jika tidak ada CSRF token maka form yang disubmit user tidak akan di-crosscheck oleh server sehingga Django akan menolaknya karena rawan dari serangan eksternal.

### Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }}) ?

    Jawabannya adalah bisa, dengan cara manual menggunakan html pertama kita menginisiasi form dengan method POST menggunakan tag `<form method="POST">` dan pastinya kita menggunakan `{% csrf_token %}`. Lalu buatlah tag table yang berisi <tr>, di dalam <tr> tersebut kita menggunakan tag input yang isinya sesuai dengan kebutuhan kita. Setalah itu tambahkan button submit untuk mengirimkan data.

### Alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

    User menginput data dan menekan button submit. Request telah dikirim berbentuk POST yang nantinya akan dihandle oleh fungsi pada views.py. Pada fungsi-fungsi tersebut, akan dilakukan pengolahan/pembacaan data , penyimpanan database, dan pengaksesan database. 
    Akses ke database  dimasukkan dalam `context` sehingga dapat dikirim ke template. Template menggunakan `context` untuk mendapatkan informasi yang dibutuhkan dan menampilkan kepada pengguna melalui fungsi di views.py yang sudah me-render informasi tersebut.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

    1. Menjalankan `python manage.py startapp todolist` di folder Tugas2PBP.
    2. Menambahkan `path('todolist/', include('todolist.urls')),` di urls.py. .project django agar route dengan url yang ada di todolist dan menjalankan fungsi show_todo yang ada di `todolist/views.py`.
    3. Membuat class di `todolist/models.py` dan membuatnya field yang berisi user, date, title, description
    4. Membuat fungsi login, logout, register yang masing masing terhubung dengan login.html dan register.html dan membuat restriksi agar user harus login dahulu dengan menambahkan `@login_required(login_url='/todolist/login/')` diatas fungsi show_todolist dan create_tasl
    5. Implementasi form registrasi, login, dan logout sama seperti pada tutorial Lab 3
    6. Mengedit bagian html agar menampikan user dengan mengakses variable yang ada di contexx (`{{username}}`) dan membuat dua buah button yang masing-masing memiliki logical command untuk logout, tambah task baru, dan membuat tabel untuk menampilkan data-data todolist yang sudah disubmit ke database.
    7. Ketika user memencet tombol tambah task, user akan diarahkan ke halaman baru `todolist/create-task` dan akan membuat form yang berisi task dan description yang akan dikirim ke fungsi create di views.py untuk ditambahkan ke database.
    8. Membuat routing agar terhubung dengan fungsi fungsi yang ada di views py ketika mengakses link todolist/register, login, create-task,logout.
    9. Deploy ke heroku dengan cara push ke repositori git lalu membuat 2 user dengan masing-masing 3 dummy list to do.

    USER 1
    username : tom
    password : tom12345

    USER 2
    username : bob
    password : bobthebuilder
