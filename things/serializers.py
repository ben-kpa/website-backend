from rest_framework import serializers
from .models import Thing


class ThingSerializerList(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "creator",
            "created_date",
            "updated_date",

            "thing_title",
            "thing_text",
        )
        model = Thing


class ThingSerializerDetails(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "creator",
            "created_date",
            "updated_date",

            "thing_title",
            "thing_text",
        )
        model = Thing
