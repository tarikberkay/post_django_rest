
# DRF Post 

Django Rest Framework ile Post, Author ve Tag gibi modüllerin bulunduğu Post Api projesi.




## Kurulum

Not: Sol taraftaki veriler Mac kurulumu için sağ taraftaki veriler Windows kurulumu içindir.

Projeyi Kurma  

```bash
  git clone https://github.com/tarikberkay/post_django_rest.git
```

Sanal Ortam Oluşturma
```bash
  python3 -m venv venv || python -m venv venv
```

Sanal Ortamı Aktif Etme
```bash
  source venv/bin/activate  ||  venv\Scripts\activate
```

Gerekli Paketleri Kurma
```bash
  pip3 install -r requirements.txt  ||  pip install -r requirements.txt
```

Gerekli dizine geçme
```bash
  cd blog_rest/
```

Projeyi Çalıştırma
```bash
  python3 manage.py runserver || python manage.py runserver
```

  
## API Kullanımı

#### Tüm öğeleri getir

```http
  http://127.0.0.1:8000/api/
```

<img src="https://github.com/tarikberkay/post_django_rest/blob/main/images/Posts.png" alt="Posts" width="450" height="450">

Post'ları getirir.

#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/tags/
```

<img src="https://github.com/tarikberkay/post_django_rest/blob/main/images/Tags.png" alt="Tags" width="450" height="450">

Tag'leri getirir.

#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/authors/
```

<img src="https://github.com/tarikberkay/post_django_rest/blob/main/images/Authors.png" width="450" height="450">

Authors'ları getirir.


#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/docs/
```
Swagger ile API'nin belgelenmesi sağlanmıştır.


#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/schema/
```
API belgesi indirilebilir.


  
