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
  
  ```json
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
  
