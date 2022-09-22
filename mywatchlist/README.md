# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

[HerokuAPP_HTML](https://django-tugaspbp2raspati.herokuapp.com/mywatchlist/html/)

[HerokuAPP_JSON](https://django-tugaspbp2raspati.herokuapp.com/mywatchlist/json/)

[HerokuAPP_XML](https://django-tugaspbp2raspati.herokuapp.com/mywatchlist/xml/)

### Perbedaan HTML, JSON, dan XML

1. HTML <br>
  HTML adalah bahasa standar pemrogaman yang digunakan untuk membuat halaman website, yang diakses melalui internet. Singkatan dari "Hypertext Markup Language" atau "bahasa markup". Bahasa markup ini mengacu pada cara tag yang digunakan, untuk menentukan tata letak halaman dan elemen di dalam halaman.

  ```html
  <html>
  <body>

  <p>This is a paragraph.</p>
  <p>This is a paragraph.</p>
  <p>This is a paragraph.</p>

  </body>
  </html>
  ```
 2. JSON <br>
  JavaScript object notation atau JSON adalah format yang digunakan untuk menyimpan dan mentransfer data. Berbeda dengan XML (extensive markup language) dan format lainnya yang memiliki fungsi serupa, JSON memiliki struktur data yang sederhana dan mudah dipahami. Itulah mengapa JSON sering digunakan pada API.
  
  ```
    ...
  {
        "model": "mywatchlist.MyWatchListItem",
        "pk": 1,
        "fields": {
            "watched": "yes",
            "title": "Shawsank Redemption",
            "rating": 5,
            "release_date": "1994",
            "review": "The Shawshank Redemption has great performances, extremely well written script and story all leading to a deeply emotional climax"
        }
    },
    ...
  ```
3. XML <br>
  Extensible Markup Language (XML) adalah bahasa komputer yang dibuat oleh World Wide Web Consortium (W3C) untuk menyederhanakan proses pertukaran dan penyimpanan data. Hal ini disebabkan keunikan dan perbedaan sistem yang digunakan oleh masing-masing server yang terhubung ke internet. Maka dari itu, diperlukan adanya standardisasi  proses transfer data antar server.
  
  ```xml
  
  ...
  
  <object model="mywatchlist.mywatchlistitem" pk="1">
        <field name="watched" type="TextField">yes</field>
        <field name="title" type="TextField">Shawsank Redemption</field>
        <field name="rating" type="FloatField">5.0</field>
        <field name="release_date" type="TextField">1994</field>
        <field name="review" type="TextField">The Shawshank Redemption has great performances, extremely well written script and story all leading to a                                                       deeply emotional climax</field>
    </object>
  ...
  ```
### Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?  

  Misal sebuah data disimpan di suatu server ,tanpa data delivery data dari database tidak akan bisa ditampilkan di sisi frontend .Untuk mengirimkan data ke sisi user, harus ada data delivery yang dikirim dari server ke user. Selain masalah tersebut ada juga kasus dimana data tersebut bisa saja berubah-ubah sepanjang jalan. Karena data sudah tersimpan di sever, data tersebut bisa diganti tanpa masalah, kemudian data tersebut bisa di-deliver ke user.
  
### Implementasi Checklist Tugas 3

1. Membuat app django baru dengan command `python manage.py startapp mywatchlist` lalu masukan `mywatchlist` ke list `INSTALLED_APPS` yang ada di `settings.py` pada folder `project_django`.

2. Menambahkan path mywatchlist sehingga app dapat diakses pada localhost, tambahkan path di urls.py di project_django
   ```
    urlpatterns = [
        ...
        path("mywatchlist/", include("mywatchlist.urls"))
        ...
    ]
   ```
 3. Buat sebuah model MyWatchList pada models.py seperti berikut
   
   ```
    class MyWatchList(models.Model):
        watched = models.TextField()
        title = models.TextField()
        rating = models.FloatField()
        release_date = models.TextField()
        review = models.TextField()
   ```
   
 4. Buat sebuah folder bernama `fixtures` di folder tersebut kita buat file `initial_mywatchlist_data.json`. File ini berfungsi untuk menyimpan 10 entri data awal `mywatchlist` yang berisikan film yang pernah ditonton ataupun tidak pernah ditonton. Setelah itu, load data tersebut dengan menjalankan command `python manage.py loaddata initial_mywatchlist_data.json`. 
 
 5. Buat fungsi `show_json`, `show_xml`, dan `show_html` pada `views.py` yang melakukan querying models `MyWatchList` yang telah dibuat dan mereturn data berbentuk HTML, XML, dan JSON. 
 
 `Untuk HTML`<br>
 
 ```html
  def show_html(request):
    data_mywatchlist_item = MyWatchListItem.objects.all()
    context = {
        'movie_list': data_mywatchlist_item,
        'nama': 'Raspati Mahatma K.D (Tommy)',
        'id': '2106750244'
    }
    return render(request, "mywatchlist.html", context)
  ```
  
  `Untuk XML`<br>
  
  ```xml 
    def show_xml(request):
      data = MyWatchListItem.objects.all()
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
  ```
  
  `Untuk JSON`<br>
  
  ```
    def show_json(request):
      data = MyWatchListItem.objects.all()
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  ```
  6. Membuat routing sehingga data di atas dapat diakses melalui URL dengan cara menambahkan berikut pada urls.py di folder mywatchlist
    ```
    urlpatterns = [
        path("", show_mywatchlist, name="showmywatchlist"),
        path("html/", show_htmtl, name="show_html"),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
    ]
    ```
7. Membuat test unit dengan `tests.py` untuk tiap path dengan format file yang berbeda. Untuk menjalankan testnya lakukan command `python manage.py test`.
8. Lakukan uji pengaksesan URL `localhost:8000` untuk 3 path format file yang telah ditambahkan menggunakan Postman. 
watchlist_html![gambar](https://user-images.githubusercontent.com/89284213/191653735-8e7a88fc-a97f-4d84-a330-b7b3c02c6abe.png)
watchlist_json![gambar](https://user-images.githubusercontent.com/89284213/191653770-7246ca68-057f-42cd-88ea-05363a416568.png)
watchlist_xml![gambar](https://user-images.githubusercontent.com/89284213/191653785-657c290c-c6dc-4574-a267-1a9762268ce2.png)

