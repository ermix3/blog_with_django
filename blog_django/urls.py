from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

# from articles.views import article_list

urlpatterns = [
    # path('', article_list, name="home"),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    path('admin/', admin.site.urls),

    path('articles/', include('articles.urls')),

    path('accounts/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'blog_django.views.notFound'
