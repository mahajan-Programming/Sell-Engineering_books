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
    semister=(
        ('Sem1','Sem1'),
        ('Sem2','Sem2'),
        ('Sem3','Sem3'),
        ('Sem4','Sem4'),
        ('Sem5','Sem5'),
        ('Sem6','Sem6'),
        ('Sem7','Sem7'),
        ('Sem8','Sem8')
    )    
    BookName=models.CharField(max_length=200,default="")
    Price=models.IntegerField(default=0)
    Year=models.CharField(max_length=10,default="")
    Tag1=models.CharField(max_length=50,choices=branch,default="")
    Tag2=models.CharField(max_length=15,choices=semister,default="")
    BookImage = models.ImageField(blank=True)
    def __str__(self):
        return str(self.pk) + '. ' + self.BookOwner.username.username+ ' ' + self.BookName
