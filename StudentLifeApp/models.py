from django.db import models
# Create your models here.
class students(models.Model):
    categAgeGroup = (
        ('Younger than 17 years','Younger than 17 years'),
        ('17 to 20 years','17 to 20 years'),
        ('21 a 23 years','21 a 23 years'),
        ('Older than 23 years','Older than 23 years'),
    )
    categGender = (
        ('Male','Male'),
        ('Female','Female'),
    )
    categArea = (
        ('Social Sciences','Social Sciences'),
        ('Life Sciences','Life Sciences'),
        ('Engineering','Engineering'),
        ('Mathematics','Mathematics'),
    )
    categYear = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    id = models.CharField(primary_key=True, max_length=4)
    gender = models.CharField(max_length=6, choices = categGender) 
    ageGroup = models.CharField(max_length=40, choices = categAgeGroup)
    year = models.CharField(max_length=2, choices = categYear)
    area = models.CharField(max_length=40, choices = categArea)
    managed = False
    db_table = 'students'