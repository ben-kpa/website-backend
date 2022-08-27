from django.urls import path
from .views import UserList, UserFromEmailDetail


urlpatterns = [
    path("users/", UserList.as_view()),
    path("user/<str:username>/", UserFromEmailDetail.as_view()),
]
