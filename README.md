
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
  source venv/bin/activate  ||  venv/scripts/bin/activate
```

Gerekli Paketleri Kurma
```bash
  pip3 install -r requirements.txt  ||  pip install -requirements.txt
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
  http://127.0.0.1:8000/posts/
```

<img src="django_rest/images/Posts.png" alt="Posts" width="320" height="180">

Post'ları getirir.

#### Öğeyi getir

```http
  http://127.0.0.1:8000/posts/tags/
```

<img src="django_rest/images/Tags.png" alt="Tags" width="320" height="180">

Tag'leri getirir.

#### Öğeyi getir

```http
  http://127.0.0.1:8000/posts/authors/
```

<img src="django_rest/images/Authors.png" alt="Authors" width="320" height="180">

Authors'ları getirir.




  
