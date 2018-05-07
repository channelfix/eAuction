from django.urls import path
from . import views
from livestream.views import AuctioneerView, BidderView

app_name = 'livestream'
urlpatterns = [
	path('', views.index, name = 'home'), # Location for main page
	path('auctioneer/', AuctioneerView.as_view(), name = 'auctioneer'), # Location for auctioneer page.
	path('bidder/', BidderView.as_view(), name = 'bidder'), # Location for bidder page.
	path('start_archive/', views.start_archive, name = 'start_archive'), # Location for start recording the video.
	path('end_archive/', views.end_archive, name = 'end_archive'), # Location for end recording the video.
]