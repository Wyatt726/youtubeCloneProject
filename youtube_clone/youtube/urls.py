from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('youtube/', views.VideoList.as_view()),

]