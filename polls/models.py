from django.db import models

# Create your models here.

class User(models.Model):
    '''用户表'''
    #
    # gender = (
    #     ('male', '男'),
    #     ('female', '女'),
    # )

    Name = models.CharField(max_length=128, unique=True)
    Nationality = models.CharField(max_length=128)
    Email = models.EmailField(unique=True)
    Wallet = models.CharField(max_length=256)
    # KYC_CERTIFICATION = models.ImageField()
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.name

