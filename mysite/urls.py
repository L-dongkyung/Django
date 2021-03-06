"""mysite URL Configuration

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
from django.urls import path, include
from mysite.views import HomeView
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import UserCreateView, UserCreateDoneTV


'''
bookmark 임포트
from bookmark.views import BookmarkLV, BookmarkDV
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
'''
from django.conf.urls import url
from bookmark import views

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    

    # class-based views (모델.py에 클래스나 함수 정의 후 불러오기)
    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    # path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),

    # urls with view definition (모델.py 정의 없이 바로 뷰에서 흐름 입력)
    # path('bookmark/', ListView.as_view(model=Bookmark), name='index'),
    # path('bookmark/<int:pk>/', DetailView.as_view(model=Bookmark), name='detail'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)