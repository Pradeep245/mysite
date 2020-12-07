from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class blog_post(models.Model):
    title = models.CharField(max_length=40)
    text = RichTextField(blank=True, null=True)
    img = models.ImageField(null=True, blank=True,upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

