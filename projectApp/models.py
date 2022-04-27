from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  User


# Create your models here.

GENDER_choices = (
	('male','MALE'),
	('female','FEMALE'),
	('other','OTHER'),
)

GENRE_choices = (
	('publicspeaking','PUBLIC SPEAKING'),
	('confidencebuilding','CONFIDENCE BUILDING'),
	('selfesteem','SELF ESTEEM'),
	('networking','NETWORKING'),
	('marketing','MARKETING'),
	('problemsolving','PROBLEMSOLVING'),
)

class userInfo(models.Model):
	#userId = models.CharField(primary_key = True, max_length = 25, unique=True)
	name = models.CharField(max_length=50)
	user = models.OneToOneField(User, primary_key=True, related_name='profile', on_delete=models.CASCADE)
	dateofbirth = models.DateField()
	emailId = models.EmailField(max_length = 75)
	profession = models.TextField()
	gender = models.CharField(max_length=50,choices = GENDER_choices, default = 'female')
	phonenumber = models.CharField(max_length = 10)
	
	def __str__(self):
		return  str(self.user)

class genre(models.Model):
	genreId = models.AutoField(primary_key = True)
	genre = models.CharField(max_length=50,choices = GENRE_choices, default = 'networking')

	def __str__(self):
		return str(self.genre)

class courses(models.Model): 
	courseId = models.AutoField(primary_key = True)
	genre = models.ManyToManyField(genre)
	authorId = models.ForeignKey(userInfo, on_delete = models.CASCADE)
	dateposted = models.DateTimeField(default = timezone.now)
	courseDesc = models.TextField()
	title = models.CharField(max_length = 50)
	posted = models.BooleanField(default = False)
	views= models.IntegerField()
	upvotes = models.IntegerField()
	downvotes = models.IntegerField()

	def __str__(self):
		return str(self.title)

class comments(models.Model):
	commentId = models.AutoField(primary_key = True)
	courseId = models.ForeignKey(courses,on_delete=models.CASCADE)
	comment_data = models.TextField()
	upvotes = models.IntegerField(blank=True)
	downvotes = models.IntegerField(blank=True)
	userId = models.ForeignKey(userInfo, on_delete = models.CASCADE)
	datecommented = models.DateTimeField(default = timezone.now)
                                                                                                   
	def __str__(self):
		return str(self.commentId)