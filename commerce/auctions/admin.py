from django.contrib import admin
from .models import User, Bid, AuctionListing, Comment
# Register your models here.

admin.site.register(User)
admin.site.register(Bid)
admin.site.register(AuctionListing)
admin.site.register(Comment)