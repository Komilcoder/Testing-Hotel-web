from django.db import models

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=400)
    text = models.TextField()
    image1 = models.ImageField(upload_to='media/static')
    image2 = models.ImageField(upload_to='media/static')


    def __str__(self):
        return self.name



class LocalGuest(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=250)
    text = models.TextField()


    def __str__(self):
        return self.name
            


class Package(models.Model):
    name = models.CharField(max_length=200 , null=True)
    text = models.TextField()
    price = models.DecimalField(max_digits=25, decimal_places=3)
    image1 = models.ImageField(upload_to='service', blank=True)
    image2 = models.ImageField(upload_to='service', blank=True)
    location = models.TextField(null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    restaurant_food = models.TextField()
    travel_news = models.TextField()
    modern_tech = models.TextField()
    product = models.TextField()
    health_care= models.TextField()



class Blog(models.Model):
    photo = models.ImageField(upload_to='blog', blank=True)
    name = models.CharField(max_length=200, null=True,blank=True)
    text = models.TextField()
    image1 = models.ImageField(upload_to='blog',blank=True)
    image2 = models.ImageField(upload_to='blog', blank=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
   
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name
       


class ToursitBlog(models.Model):
    photo = models.ImageField(upload_to='blog',null=True)
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=150)
    text = models.TextField()
    image1 = models.ImageField(upload_to = 'blog')
    image2 = models.ImageField(upload_to='blog')
    image3 = models.ImageField(upload_to = 'blog')


    def __str__(self):
        return self.name
    


        
            
    


    