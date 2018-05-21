from django.urls import path
from . import views
from livestream.views import AuctioneerView, BidderView

app_name = 'lvs'
urlpatterns = [
    # Location for main page
    path('', views.index, name='home'),
    # Location for auctioneer page.
    path('auctioneer/', AuctioneerView.as_view(), name='auctioneer'),
    # Location for bidder page.
    path('bidder/', BidderView.as_view(), name='bidder'),
    # Location for start recording the video.
    path('start_archive/', views.start_archive, name='start_archive'),
    # Location for end recording the video.
    path('end_archive/', views.end_archive, name='end_archive'),
]