from django.db import models
from django.utils import timezone
from hitcount.models import HitCountMixin, HitCount
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"


    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='yangilikuzapp/images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="Free", null=True, verbose_name="category")
    publish_time = models.DateTimeField(default=timezone.now)
    creatid_time = models.DateTimeField(auto_now_add=True)
    updates_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                            choices=Status.choices,
                            default=Status.Draft)
    view_count = models.IntegerField(default=0)

    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single', args=[int(self.id)])

#comment model
class Comment(models.Model):
    post = models.ForeignKey(News,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body)


class contact(models.Model):
    ism = models.CharField(max_length=255)
    elektron_pochta = models.EmailField(max_length=255)
    sarlavha = models.CharField(max_length=255)
    xabar = models.TextField()

    def __str__(self):
        return self.name


class ViewCount(models.Model):
    ip_address = models.GenericIPAddressField()