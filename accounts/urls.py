from django.urls import path
from .views import signUpView, logInView, logOutView

app_name = 'accounts'

urlpatterns = [
    path('signup/', signUpView, name='signup'),
    path('login/', logInView, name='login'),
    path('logout/', logOutView, name='logout'),
]
