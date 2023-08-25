from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_page/", views.newPage, name = "new_page"),
    path("wiki/<str:page_name>",views.visitPage,name="page"),
    path("random_page",views.randomPage,name="random_page"),
    path("search", views.search,name="search"),
    path("add", views.add,name="add"),
    path("wiki/<str:page_name>/edit",views.editPage,name = "edit")
]
