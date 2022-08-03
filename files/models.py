from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=200)
    files = models.FileField()
    image_one = models.ImageField(upload_to='images/', null=True, blank=True)
    image_two = models.ImageField(upload_to='images/', null=True, blank=True)
    image_three = models.ImageField(upload_to='images/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_name +" "+ self.user.username

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])