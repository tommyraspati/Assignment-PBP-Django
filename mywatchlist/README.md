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
