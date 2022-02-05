from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Creating a Post and comment model.
# Adding in columns to data table, including dates created / published, and
# the type / genre of country shown. Character field, include as dropdown in forms.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    type = models.CharField(max_length=200,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
        # Approves the comments from the comments model.

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})


    def __str__(self):
        return self.title

# Include a rating 0-5 stars. So users can rate suggested music / albums.

class Comment(models.Model):
    post = models.ForeignKey('pro1.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    rating = models.IntegerField(default=1,validators=[MinValueValidator(0),MaxValueValidator(5)]
    )

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
