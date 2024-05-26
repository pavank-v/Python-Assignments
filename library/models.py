from django.db import models
from django.contrib.auth.models import User
from .book_details import BookDetails


#Setting default User
default_user = User.objects.get(username='default_user')

#Model for Storing the booksin Favorite page
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=default_user.id)
    title = models.CharField(max_length=100)
    amazon_url = models.URLField(blank=True)
    flipkart_url = models.URLField(blank=True)
    good_reads_review = models.CharField(blank=True,max_length=10,null=True)
    cover_image = models.URLField(blank=True)
    
    #Method to save the Additional Details
    def custom_save(self, *args, **kwargs):
        details = BookDetails(self.title)
        self.amazon_url = details.amazon_link()
        self.flipkart_url = details.flipkart_link()
        self.good_reads_review = details.good_reads_review()
        self.cover_image = details.cover_image()
        self.save(*args, **kwargs)
    
    def __str__(self):
        return self.title
        
#Model for saving the Search History
class SearchHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=default_user.id)
    title = models.CharField(max_length=100)
    amazon_url = models.URLField(blank=True)
    flipkart_url = models.URLField(blank=True)
    good_reads_review = models.CharField(blank=True,max_length=10,null=True)
    cover_image = models.URLField(blank=True)
    
    #Method to save the Additional Details
    def custom_save(self, *args, **kwargs):
        details = BookDetails(self.title)
        self.amazon_url = details.amazon_link()
        self.flipkart_url = details.flipkart_link()
        self.good_reads_review = details.good_reads_review()
        self.cover_image = details.cover_image()
        self.save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
