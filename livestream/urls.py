from django.urls import path
from . import views


app_name = 'livestream'
urlpatterns = [
    # Creating Livestream page.
    path('create_livestream/', views.LivestreamView.as_view(), name='livestream_created'),
    # Collection of Livestream
    path('auction_events/', views.LivestreamListView.as_view(), name='livestream_lists'),
    # Used to start the Auction.
    path('initiate_auction/', views.AuctionView.as_view(), name='auction_view'),
    # Store the logs
    path('store_logs/', views.LogStorageView.as_view(), name='log_storage'),
    # Retrieve the logs
    path('show_logs/', views.RetrievedLogView.as_view(), name='show_log'),
    # Delete logs for certain Auction
    path('end_auction/', views.AuctionDestroyedView.as_view(), name='end_auction'),
    # Get all the list of products
    path('product_list/', views.ProductListView.as_view(), name='product_list')
]
