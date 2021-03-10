from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<str:name>", views.greet, name='greet'),
    path("bleddyn", views.bleddyn, name='bleddyn'),
    path("david", views.david, name='david')
]