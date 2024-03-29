from django.urls import path 
from posts.views import PostView, TagView, AuthorView, PostDetailView

urlpatterns = [
    path('', PostView.as_view()),
    path('<int:id>/',PostDetailView.as_view()),
    path('tags/', TagView.as_view()),
    path('authors/', AuthorView.as_view())
]
