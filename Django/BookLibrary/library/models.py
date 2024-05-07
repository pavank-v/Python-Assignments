from django.db import models
from django.contrib.auth.models import User

from .scrapping import BookDetails

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "List of Users"
        
    def __str__(self):
        return self.email
    

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    amazon_url = models.URLField(blank=True)
    flipkart_url = models.URLField(blank=True)
    good_reads_review = models.CharField(blank=True,max_length=10,null=True)
    cover_image = models.URLField(blank=True)
    
    def save(self, *args, **kwargs):
        details = BookDetails(self.title)
        self.amazon_url = details.amazon_link()
        self.flipkart_url = details.flipkart_link()
        self.good_reads_review = details.good_reads_review()
        self.cover_image = details.cover_image()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
       
class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    amazon_url = models.URLField(blank=True)
    flipkart_url = models.URLField(blank=True)
    good_reads_review = models.CharField(blank=True,max_length=10,null=True)
    cover_image = models.URLField(blank=True)
    
    def save(self, *args, **kwargs):
        details = BookDetails(self.title)
        self.amazon_url = details.amazon_link()
        self.flipkart_url = details.flipkart_link()
        self.good_reads_review = details.good_reads_review()
        self.cover_image = details.cover_image()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
