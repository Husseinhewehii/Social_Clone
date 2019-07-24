"""social_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',v.Home_View.as_view(),name='home'),
    path('test/',v.Test_Page.as_view(),name='test'),
    path('thanks/',v.Thanks_Page.as_view(),name='thanks'),
    path('accounts/',include('accounts.urls'),name='accounts'),
    path('accounts/s',include('django.contrib.auth.urls')),
    path('posts/',include('posts.urls'),name='posts'),
    path('groups/',include('groups.urls'),name='groups'),
]
