from django.db import models

# Create your models here.


class Student(models.Model):
    
    ad = models.CharField(max_length=50,null=True,blank=True)
    metn = models.TextField(max_length=700,null=True,blank=True)
    tarix = models.DateField(auto_now=True)
    
    
    def __str__(self):
        return self.ad
    
class Telefon(models.Model):
    
   
    model = models.CharField(max_length=100,null=True,blank=True)
    dioqonal = models.CharField(max_length=100,null=True,blank=True)
    prosessor = models.CharField(max_length=100,null=True,blank=True)
    nuve_sayi = models.CharField(max_length=100,null=True,blank=True)
    ram = models.CharField(max_length=100,null=True,blank=True)
    img = models.FileField(upload_to = "images/")
    
    
    def __str__(self):
        return self.model
    

class Shop(models.Model):
    ad = models.CharField(max_length=50)
    img = models.FileField(upload_to='images/',null=True,blank=True)
    tel = models.ForeignKey(Telefon,on_delete = models.CASCADE)
    
    def __str__(self) :
        return  self.ad
    
    
class Category(models.Model):
    ad = models.CharField(max_length=50,blank=True, null=True)
    
    def __str__(self) :
        return  self.ad
    
class Item(models.Model):
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    al = models.IntegerField()
    sat = models.IntegerField()
    miqdar = models.IntegerField()
    
    
    
    @property
    def cem(self):
        qazanc = (self.sat - self.al) * self.miqdar
        return qazanc
        
        