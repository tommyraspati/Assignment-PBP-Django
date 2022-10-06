# Tugas 4 Pengimplementasian Form dan Autentikasi Menggunakan Django

[HerokuAPP](https://django-tugaspbp2raspati.herokuapp.com/todolist/)

### Kegunaan {% csrf_token %} pada elemen <form>

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

# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

### Perbedaan dari Inline, Internal, dan External CSS? 

1. Inline CSS adalah mengaplikasikan style kepada elemen anggota suatu halaman HTML dengan menaruh style sebagai attribute dalam tag. Metode ini efektif digunakan jika hanya sebatas menambahkan styling pada 1 selector yang digunakan dan tidak akan digunakan lagi. Kekurangannya adalah hanya satu elemen yang berubah sehingga jika ingin mengaplikasikan style ke semua elemen, inline CSS harus diterapkan ke semua elemen.

2. Internal CSS kode CSS-nya ditaruh pada di file HTMLnya. CSS internal diletakkan di dalam tag <style></style>. Kelebihannya Tidak perlu meng-upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama dan Perubahan hanya terjadi pada 1 halaman. Kekurangannya adalah perubahan hanya terjadi pada 1 halaman – tidak efisien bila Anda ingin menggunakan CSS yang sama pada beberapa file.

3. External CSS adalah menambahkan CSS ke website Anda adalah dengan menghubungkannya ke file .CSS eksternal. Apapun yang Anda buat pada file CSS akan tampil pada website Anda secara keseluruhan. Keuntungannya adalah file CSS yang sama bisa digunakan di banyak halaman. Kekurangannya adalah halaman belum tampil secara sempurna hingga file CSS selesai dipanggil.

### Tag HTML5 yang kamu ketahui

1. `<button>` - Tag ini akan membuat sebuah kotak yang dapat ditekan layaknya tombol.
2. `<h1>` ... `<h6>` - Teks yang diapit oleh tag ini akan tampil sebagai heading/sub-heading. Ukuran teks `<h1>` paling besar dan ukuran teks `<h6>` paling kecil.
3. `<div>` - Tag ini dapat membungkus dan memisahkan elemen-elemen lain.
4. `<canvas>` digunakan sebagai kanvas atau dasar untuk menggambar animasi ataupun elemen grafis lainnya.

### Tipe-tipe CSS selector yang kamu ketahui

1. Element selector, element selector memilih elemen HTML berdasarkan nama elemen.
2. Id selector, id selector menggunakan atribut id dari elemen HTML untuk memilih elemen tertentu. Id dari sebuah elemen unik dalam sebuah halaman, jadi id selector digunakan untuk memilih satu elemen unik!
3. Class selector, class selector memilih elemen HTML dengan atribut kelas tertentu.

### Implementasi checklist
1. Import Bootstrap ke dalam template
Tempatkan tag `<link>` di `<head>` untuk CSS kami, dan tag `<script>` untuk bundel JavaScript  sebelum penutup di `</body>` dalam `base.html`.

```html
<head>
    ...
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    ...
</head>
<body>
    ...
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
</body>
```

2. Kustomisasi halaman-halaman todolist
Menambahkan fitur-fitur dari bootstrap seperti buttons, cards, navbar, dan warna-warna.

3. Membuat halaman yang responsif
menambahkan tag `<meta name="viewport" content="...">` untuk mengatur viewport dari browser sehingga sifat responsive, khususnya pada perangkat mobile, dapat terjadi dengan benar.