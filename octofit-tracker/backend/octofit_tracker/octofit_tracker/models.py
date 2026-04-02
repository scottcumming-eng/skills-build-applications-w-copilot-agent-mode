from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	email = models.EmailField(unique=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	members = models.ManyToManyField('User', related_name='teams')
	def __str__(self):
		return self.name

class Activity(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	activity_type = models.CharField(max_length=100)
	duration = models.IntegerField()
	def __str__(self):
		return f"{self.user.email} - {self.activity_type}"

class Leaderboard(models.Model):
	team = models.ForeignKey('Team', on_delete=models.CASCADE)
	points = models.IntegerField()
	def __str__(self):
		return f"{self.team.name}: {self.points}"

class Workout(models.Model):
	name = models.CharField(max_length=100)
	difficulty = models.CharField(max_length=50)
	def __str__(self):
		return self.name
