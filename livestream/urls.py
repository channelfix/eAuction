from django.urls import path
from . import views
# from livestream.views import AuctioneerView, BidderView

app_name = 'livestream'
urlpatterns = [
    # Location for main page
    path('', views.IndexView.as_view(), name='home'),
    # Location for auctioneer page.
    path('auctioneer/', views.AuctioneerView.as_view(), name='auctioneer'),
    # Location for bidder page.
    # path('bidder/', views.BidderView.as_view(), name='bidder'),
    # # Location for start recording the video.
    # path('start_archive/', views.start_archive, name='start_archive'),
    # # # Location for end recording the video.
    # path('end_archive/', views.end_archive, name='end_archive'),
]
