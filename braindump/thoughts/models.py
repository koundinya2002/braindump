from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Thoughts(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.owner) + " | " + str(self.title)