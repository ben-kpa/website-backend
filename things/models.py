from django.db import models
from accounts.models import CustomUser


class Thing(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    thing_title = models.CharField(max_length=250, blank=True)
    thing_text = models.TextField(max_length=2500, blank=True)

    def __str__(self):
        if self.thing_title:
            return self.thing_title
        untitled_name = 'Untitled'
        if self.thing_title is None:
            return untitled_name
        if self.thing_title == '':
            return untitled_name

