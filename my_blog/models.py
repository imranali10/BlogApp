from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    desc = models.CharField(max_length=220, null=True)
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
