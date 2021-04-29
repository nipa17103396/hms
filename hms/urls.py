"""hms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="core/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="core/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="core/password_reset_done.html"), name ='password_reset_complete'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="core/password_reset.html"), name='password_reset'),
    path('', include('django.contrib.auth.urls')),
    path('base/', views.Base.as_view(),name='base'),
    path('about/', views.About.as_view(), name='about'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('dep/', views.Dep.as_view(), name='dep'),
    path('doctor/', views.Doctor.as_view(), name='doctor'),
    path('elements/', views.Elements.as_view(), name='elements'),
    path('', views.Index.as_view(), name='index'),
    path('services/', views.Services.as_view(), name='services'),
    path('single_blog/', views.Single_blog.as_view(), name='single_blog'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', views.ActivateURL, name='activate'),
    path('appointment/', views.Appoinment.as_view(), name='appointment'),
]
