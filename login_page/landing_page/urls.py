from django.urls import path
from . import views

urlpatterns = [
        path('login/', views.login_user, name="login_user"),
        path('signup/', views.signup, name='signup'),
        path('signout/', views.signout, name='signout'),
]
