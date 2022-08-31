from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "created_date", "updated_date")


class UserSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "created_date", "updated_date")
