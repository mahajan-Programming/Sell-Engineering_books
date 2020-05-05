from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPersonalInfo(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 
    PhoneNo = models.CharField(max_length=100,default="")
    City = models.CharField(max_length=20,default="")
    Institute=models.CharField(max_length=50,default="")
    SubUrb=models.CharField(max_length=30,default="")
    def __str__(self):
        return str(self.pk) + '. ' + self.username.username



class NewBook(models.Model):
    BookOwner = models.ForeignKey(UserPersonalInfo,on_delete=models.CASCADE,related_name="owner")
    year=(
        ('First Year','First year'),
        ('Second Year','Second Year'),
        ('Third Year','Third Year'),
        ('Fourth Year','Fourth Year')
    )
    branch=(('First Year','First Year'),
            ('CSE','CSE'),
            ('IT','IT'),
            ('Entc','Entc'),
            ('Mech','Mech'),
            ('Instrumentation','Instrumentation'),
            ('Production','Production'),
            ('Chemical','Chemical'),
            ('Electrical','Electrical'),
            ('Mechatronix','Mechatronix'),
            )
    BookName=models.CharField(max_length=200,default="")
    Price=models.IntegerField(default=0)
    Year=models.CharField(max_length=10,default="")
    Tag1=models.CharField(max_length=20, choices=year, default="")
    Tag2=models.CharField(max_length=50,choices=branch,default="")
    BookImage = models.ImageField(blank=True)
    def __str__(self):
        return str(self.pk) + '. ' + self.BookOwner.username.username+ ' ' + self.BookName
