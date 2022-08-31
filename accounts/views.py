from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from .serializers import UserSerializerList, UserSerializerDetail


class UserList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializerList


class UserFromEmailDetail(generics.RetrieveUpdateDestroyAPIView): # new
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializerDetail
    lookup_field = 'username'
