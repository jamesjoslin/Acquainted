from django.db import models
from django.contrib.auth.models import User
from django.forms.fields import Field
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

# this is where i create my post objects. the guts of what i want every object in a class to look like
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='media/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)

    #what the post will show to title itself
    def __str__(self):
        return self.title + "  |  " + str(self.author)

    #what happens when a model is created. sends me to the post's page
    def get_absolute_url(self):
        return reverse('post-details', args=(str(self.id)))

    #ordering
    class Meta:
        ordering = ['-post_date']



