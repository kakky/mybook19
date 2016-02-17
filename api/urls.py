from django.conf.urls import url
from api import views

urlpatterns = [
    # 書籍
    url(r'^v1/books/$', views.book_list, name='book_list'),     # 一覧
]
