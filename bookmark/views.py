from django.shortcuts import render
from bookmark.models import Bookmark
from django.views.generic import ListView, DetailView

from django.shortcuts import render


# Create your views here.
# 제어 흐름 및 로직 구성


class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark
