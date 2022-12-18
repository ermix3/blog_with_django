from django.urls import path
from . import views

app_name = 'articles'  # this is the namespace of urls

urlpatterns = [
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    path('<slug:slug>/', views.article_detail, name="detail"),
]
