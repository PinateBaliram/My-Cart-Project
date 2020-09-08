from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    product_desc=models.CharField(max_length=300)
    product_category=models.CharField(max_length=300,default="")
    product_subcategory=models.CharField(max_length=300,default="")
    product_price=models.IntegerField(default=0)
    product_pub_date=models.DateField()
    product_image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70,default="")
    email=models.CharField(max_length=70,default="")
    phone=models.CharField(max_length=12,default="")
    desc=models.CharField(max_length=3000,default="")

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    json_data=models.CharField(max_length=5000,default="")
    ammount=models.IntegerField(default=0)
    name=models.CharField(max_length=111,default="")
    email=models.CharField(max_length=111,default="")
    phone=models.CharField(max_length=12,default="")
    address=models.CharField(max_length=5000,default="")
    address1=models.CharField(max_length=5000,default="")
    state=models.CharField(max_length=111,default="")
    city=models.CharField(max_length=111,default="")
    zip_code=models.CharField(max_length=111,default="")

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

class Signup(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=90,default="")
    email=models.CharField(max_length=90,default="")
    password=models.CharField(max_length=30,default="")

    def __str__(self):
        return self.username
