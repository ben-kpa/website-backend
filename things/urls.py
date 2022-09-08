from django.urls import path
from .views import ThingList, ThingDetail

urlpatterns = [
    path('<int:pk>/', ThingDetail.as_view()),
    path('', ThingList.as_view()),
]
