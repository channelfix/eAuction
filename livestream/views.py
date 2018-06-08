from opentok import OpenTok, MediaModes, Roles, OutputModes
from .models import Session, Archive, Logs
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views import View
from profiles.models import Product, Subscribed
from itertools import chain

# from pprint import pprint


class OpenTokCloudView:
    opentok_cloud = OpenTok(settings.OPENTOK_API_KEY,
                            settings.OPENTOK_API_SECRET)


class LivestreamView(OpenTokCloudView, View):
    session = ''

    def post(self, request):
        auctioneer = request.user

        # Server IP address
        session_address = "127.0.0.1"

        # Create a Session
        self.session = self.opentok_cloud.create_session(
            session_address, media_mode=MediaModes.routed)

        # Title of the Livestream
        title = request.POST.get('title', '')

        # Description of the Livestream
        description = request.POST.get('description', '')

        # Product name
        list_of_product_names = request.POST.get('product_name', '')

        # Product minimum price
        list_of_product_minimum_prices = request.POST.get('product_minimum_price','')

        product_names = list_of_product_names.split(',')
        product_minimum_prices = list_of_product_minimum_prices.split(',')

        length = len(product_names)

        # One auctioneer own one auction event
        session = Session.objects.create(auctioneer_username=auctioneer.username,
                                         title=title,
                                         description=description,
                                         session_id=self.session.session_id,
                                         is_live=True)

        for i in range(length):
            Product.objects.create(session=session, profile=profile,
                                   name=product_names[i],
                                   minimum_price=product_minimum_prices[i])

        context = {
            'auction_id': session.id,
            'auctioneer_username': auctioneer.username,
            'message': 'Livestream created'
        }

        return JsonResponse(context)


class AuctionView(LivestreamView, View):
    """ Sends the user to certain livestream """

    token = ''

    def post(self, request):
        auction_id = request.POST.get('auction_id', '')
        current_session = Session.objects.get(id=auction_id)
        # Get session id of this livestream
        session_id = current_session.session_id
        # Get list of product of this livestream
        product_list = list(current_session.auction_products.all()
                            .values('name'))

        # Add the current user to this livestream
        profile = request.user.profile
        profile.session = current_session
        profile.save()

        is_auctioneer = request.POST.get('is_auctioneer', '')

        # Check if the user is an auctioneer
        if(is_auctioneer):
            self.token = self.opentok_cloud.generate_token(session_id)
        else:
            self.token = self.opentok_cloud.generate_token(session_id,
                                                           role=Roles
                                                           .subscriber)
        # Get list of username from User via profile
        attendees_profile = list(current_session.attendees.all()
                                 .values('user__username'))

        context = {
            'api_key': settings.OPENTOK_API_KEY,
            'session_id': session_id,
            'token': self.token,
            'product_list': product_list,
            'attendees_profile': attendees_profile
        }

        return JsonResponse(context)


class LivestreamListView(View):
    """ View all the livestream for which the subcriber subscribe to """

    def get(self, request):
        bidder = request.user

        auction = Subscribed.objects.all()\
                            .filter(bidder=bidder)\
                            .values('auctioneer__username')

        sessions = Session.objects.none()

        for auctioneer in auction:
            sessions = chain(Session.objects.all()
                             .filter(auctioneer_username=auctioneer
                             ['auctioneer__username'])
                             .values('auctioneer_username', 'id',
                                     'title', 'description',
                                     'is_live'), sessions)

        sessions = list(sessions)

        return JsonResponse({'sessions': sessions})


class LogStorageView(View):
    """ Store logs """

    def post(self, request):
        auction_id = request.POST.get('auction_id', '')
        message = request.POST.get('logs', '')
        time = request.POST.get('time', '')

        Logs.objects.create(auction_id=auction_id,
                            message=message,
                            time=time)

        return HttpResponse('Stored log successfully')


class RetrievedLogView(View):
    """ Retrieves all the logs given the\
    latest auction id from certain Auciton """

    def post(self, request):
        auction_id = request.POSt.get('auction_id', '')
        latest_log_id = request.POST.get('log_id', '')

        # Initialize log with empty set
        query_logs = Logs.objects.none()

        query_logs = Logs.objects.all().filter(auction_id=auction_id)\
                                       .values('message', 'time')

        if auction_id != -1:
            query_logs = query_logs.filter(id__gt=latest_log_id)\
                                   .values('message', 'time')

        # List of logs
        logs = list(query_logs)

        return HttpResponse({'logs': logs})


class AuctionDestroyedView(View):
    def post(self, request):
        auction_id = request.POST.get('auction_id', '')

        # Delete all the logs for certain livestream
        Logs.objects.all().filter(auction_id=auction_id).delete()

        # Delete this Livestream
        Session.objects.get(id=auction_id).delete()

        return HttpResponse('Auction close')

# # start to record the video.
# def start_archive(request):
#     sessionId = Session.objects.get(pk=1).session_id

#     # Start recording the video.

#     archive = opentok_cloud.start_archive(sessionId, has_video=True,
#                                           name='Test',
#                                           output_mode=OutputModes.individual)

#     archives = Archive(archive_id=archive.id)
#     archives.save()

#     return HttpResponse('Start recording')


# # stop the video recording.
# def end_archive(request):
#     # get the id of the last archive object from Archive collections.
#     archive_id = Archive.objects.get(pk=Archive.objects.count()).archive_id
#     # Stop recording the video.
#     opentok_cloud.stop_archive(archive_id)

#     return HttpResponse('Stop recording')

# Create your views here
