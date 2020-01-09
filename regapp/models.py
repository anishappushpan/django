from django.db import models

class registration(models.Model):
    name=models.CharField(max_length=10,default="")        
    stdid=models.IntegerField()
    year=models.IntegerField(default=2017)
    address=models.CharField(max_length=50,default="")
    mobile=models.IntegerField()
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=10,default="")
    branch=models.CharField(max_length=10,default="")

    class meta:
        db_table="regapp_registration"
class admin(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=10) 
    class meta:
        db_table="regapp_admin"
class facultyreg(models.Model):
    name=models.CharField(max_length=10,default="")        
    fid=models.IntegerField(null="True",blank="True")
    address=models.CharField(max_length=50,default="",null="True",blank="True")
    mobile=models.IntegerField(null="True",blank="True")
    email=models.CharField(max_length=20,null="True")
    password=models.CharField(max_length=10,null="True")

    class meta:
        db_table:"regapp_facultyreg"
class atta(models.Model):
    name=models.CharField(max_length=10,default="")        
    stdid=models.IntegerField(null="True",blank="True")
    firstp=models.CharField(max_length=10,default="",null="True",blank="True")
    secondp=models.CharField(max_length=10)
    thirdp=models.CharField(max_length=10,default="",null="True",blank="True")
    fourthp=models.CharField(max_length=10,default="",null="True",blank="True")

    class meta:
        db_table:"atta"   
class marks(models.Model):
    name=models.CharField(max_length=10,default="")        
    stdid=models.IntegerField(null="True",blank="True")
    mark1=models.CharField(max_length=10,default="",null="True",blank="True")
    mark2=models.CharField(max_length=10)
    mark3=models.CharField(max_length=10,default="",null="True",blank="True")
    class meta:
        db_table:"marks"
class facultyleave(models.Model):
    name=models.CharField(max_length=10,default="")        
    stdid=models.IntegerField(null="True",blank="True")
    fromdate=models.DateField()
    todate=models.DateField()
    reason=models.CharField(max_length=20,default="")
    status=models.CharField(max_length=10,default="",null="True",blank="True")
    class meta:
        db_table:"leaves"  
class studentleavez(models.Model):
    name=models.CharField(max_length=10,default="")        
    stdid=models.IntegerField(null="True",blank="True")
    fromdate=models.DateField()
    todate=models.DateField()
    reason=models.CharField(max_length=20,default="")
    status=models.CharField(max_length=10,default="",null="True",blank="True")
    class meta:
        db_table:"studentleaves"                                    
# Create your models here.
