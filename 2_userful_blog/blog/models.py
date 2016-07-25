from django.db import models
from django.utils import timezone

# Create your models here.
class Members(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	is_active = models.BooleanField(default=True)

class Post(models.Model):
	title = models.CharField(max_length=70)
	author = models.CharField(max_length=50)
	content = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	member = models.ForeignKey(Members)

class Comment(models.Model):
	content = models.TextField()
	author = models.CharField(max_length=50)
	member = models.ForeignKey(Members)
	post = models.ForeignKey(Post)
	is_active = models.BooleanField(default=True)