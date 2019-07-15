from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book),
    url(r'^book$', views.book),
    url(r'^book_process$', views.book_process),
    url(r'^author$', views.author),
    url(r'^author_process$', views.author_process),
    url(r'^books/(?P<id>\d+)$', views.book_information),
    url(r'^authors/(?P<id>\d+)$', views.author_information),
    url(r'^add_book$', views.book_add)
]