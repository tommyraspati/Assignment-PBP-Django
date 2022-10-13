# Tugas 6: Javascript dan AJAX

[HerokuAPP](https://django-tugaspbp2raspati.herokuapp.com/todolist/)

###  Perbedaan antara asynchronous programming dengan synchronous programming

- _Asychronous programming_ proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Sehingga waktu eksekusi lebih cepat.

- _Synchronous programming_ adalah proses jalannya program secara sequential , disini yang dimaksud sequential ada berdasarkan antrian ekseskusi program jadi menunggu proses antrian eksekusi. Waktu jalannya program lebih lama daripada _asynchronous programming_

### Event-driven programming

Event-Driven Programming adalah salah satu teknik pemogramman, yang konsep kerjanya tergantung dari kejadian atau event tertentu. Event-Driven programming juga bisa dibilang suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya. Contoh di program: $("#form-ajax").on("submit",function(e) {}

### Penerapan asynchronous programming pada AJAX
- Menambahkan `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>` pada base html `<head>`
- Tambahkan `<script>` di dalam file html
- Ajax akan melakukan event yang telah dibuat.
- Action dan response akan dilakukan secara asynchronus oleh server
- Data akan ditampilkan pada page tanpa harus refresh lagi

### Cara implementasi checklist
- Tambahkan fungsi berikut di `views.py`:

```
@csrf_exempt
@login_required(login_url="/todolist/login/")
def add_task(request):

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        temp = Task.objects.create(
            title=title, description=description, user=request.user
        )
        return JsonResponse({
            "title": title,
            "date": temp.date,
            "description": description
        }, status=200)

def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

- Tambahkan path show_json dan add_task ke urlpatterns di urls.py
- Tambahkan script ajax di base.html
- Buat fungsi GET dan POST di `todolist.html` dengan kode sebagi berikut:
```
<script>
        $(document).ready(function(){
            $.getJSON("{% url 'todolist:show_json' %}", function(data){
                $.each(data, function(index,value){
                console.log(value)
                    $("#todolist_container").append(
                    `<div class="d-flex flex-wrap justify-content-center align-items-center ">
                            <div class="card text-center m-4"  style="width: 18rem; ">
                                <div class="card-body">
                                <h5 class="card-title">${value.fields.title}</h5>
                                <p class="card-text">${value.fields.description}.</p>
                                <p class="card-text">${value.fields.date}.</p>
                                <a href="#" class="btn btn-primary">Delete task</a>
                                </div>
                            </div>
                        </div>`    
                    )
                })
        })
        $("#form_todolist").on("submit",function(e) {
        e.preventDefault() 
        let date = $("#date").val();
        let title = $("#title").val();
        let description = $("#description").val();
        $.ajax({
          method: "POST",
          url: "/todolist/add/",
          data: {"date":date, "title":title, "description":description},
        }).done(function(resp) {
          console.log(resp)
          $("#todolist_container").append(
            `<div class="d-flex flex-wrap justify-content-center align-items-center ">
                            <div class="card text-center m-4"  style="width: 18rem; ">
                                <div class="card-body">
                                <h5 class="card-title">${resp.title}</h5>
                                <p class="card-text">${resp.description}.</p>
                                <p class="card-text">${resp.date}.</p>
                                <a href="#" class="btn btn-primary">Delete task</a>
                                </div>
                            </div>
                        </div>`    
          )
          $("#exampleModal").modal("toggle")
        });
    })
    })


</script>
```
- Tambahkan modal di `todolist.html`:
```
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Create Task</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">

        <form id="form_todolist" action = "/todolist/add/">
            {% csrf_token%}
          <div class="mb-3">
            <label class="col-form-label">Title:</label>
            <input type="text" class="form-control" id="title">
          </div>
          <div class="mb-3">
            <label  class="col-form-label">Description:</label>
            <textarea class="form-control" id="description"></textarea>
          </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="submit" value="submit" class="btn btn-primary" id="submit_btn">Submit</button>
            </div>
        </form>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
```