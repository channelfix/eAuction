from django.urls import path
from livestream.views import AuctionView, LivestreamView, LivestreamListView

app_name = 'livestream'
urlpatterns = [
    # Creating Livestream page.
    path('create_livestream/', LivestreamView.as_view(), name='livestream_created'),
    # Collection of Livestream
    path('auction_events/', LivestreamListView.as_view(), name='livestream_lists'),
    # Used to start the Auction.
    path('initiate_auction/', AuctionView.as_view(), name='auction_view'),
]
