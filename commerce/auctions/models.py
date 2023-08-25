from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

class User(AbstractUser):
    pass
class AuctionListing(models.Model):
    BOOKS = 'BO'
    CLOTHING = 'CL'
    ELECTRONICS = 'EL'
    HOME = 'HO'
    OTHER = 'OT'
    CATEGORIES_CHOICES = [
        (BOOKS, 'Books'),
        (CLOTHING, 'Clothing'),
        (ELECTRONICS,'Electronics'),
        (HOME, 'Home'),
        (OTHER, 'other')
    ]
    name = models.CharField(max_length=64)
    starting_bid = models.DecimalField(max_digits=6,decimal_places=2)
    current_bid = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='Images', default="Images/No_Image_Available.jpg")
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_datetime = models.DateTimeField()
    categories = models.CharField(max_length=2,choices=CATEGORIES_CHOICES,default=OTHER)

    
class Bid(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    auction_listing = models.ForeignKey(AuctionListing,on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=6, decimal_places=2)
class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    auction_listing = models.ForeignKey(AuctionListing,on_delete=models.CASCADE)