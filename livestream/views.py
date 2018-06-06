from opentok import OpenTok, MediaModes, Roles, OutputModes
from .models import Session, Archive
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views import View
from profiles.models import Product

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
        session = Session.objects.create(auctioneer=auctioneer,
                                         title=title,
                                         description=description,
                                         session_id=self.session.session_id)

        # Store the product to certain Session and Profile
        profile = auctioneer.profile

        for i in range(length):
            Product.objects.create(session=session, profile=profile,
                                   name=product_names[i],
                                   minimum_price=product_minimum_prices[i])

        return HttpResponse('Livestream created')


class AuctionView(LivestreamView, View):
    token = ''

    def post(self, request):
        auction_id = request.POST.get('auction_id', '')
        session_id = Session.objects.get(id=auction_id).session_id
        is_auctioneer = request.POST.get('is_auctioneer', '')

        # Check if the user is an auctioneer
        if(is_auctioneer):
            self.token = self.opentok_cloud.generate_token(session_id)
        else:
            self.token = self.opentok_cloud.generate_token(session_id,
                                                           role=Roles.subscriber)

        context = {
            'api_key': settings.OPENTOK_API_KEY,
            'session_id': session_id,
            'token': self.token,
        }

        return JsonResponse(context)


class LivestreamListView(View):
    def get(self, request):
        sessions = list(Session.objects.all().values('auctioneer', 'id','title', 'description'))

        return JsonResponse({'sessions': sessions})
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
