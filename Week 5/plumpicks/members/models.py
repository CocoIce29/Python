from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class Post(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  author = models.CharField(max_length=255)
  post_date = models.DateField(null=True)
  sport_tag = models.CharField(max_length=255)
  bet_tag = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.title}"