from opentok import OpenTok, MediaModes, Roles, OutputModes
from .models import Session, Archive
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views import View

from pprint import pprint


class OpenTokCloudView:
    opentok_cloud = OpenTok(settings.OPENTOK_API_KEY,
                            settings.OPENTOK_API_SECRET)


class LivestreamView(OpenTokCloudView, View):
    session = ''

    def post(self, request):
        auctioneer = request.user

        # Title of the Livestream
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')

        # Name and the minimum price of the product for the bid
        product_name = request.POST.get('product_name', '')
        product_price = request.POST.get('product_price', '')

        # Server IP address
        session_address = "127.0.0.1"

        # Create a Session
        self.session = self.opentok_cloud.create_session(
            session_address, media_mode=MediaModes.routed)

        auctioneer_profile_products = auctioneer.profile.products
        auctioneer_profile_products.name = product_name
        auctioneer_profile_products.minimum_price = product_price
        auctioneer_profile_products.save()

        # Store the new session id
        Session.objects.create(user=auctioneer,
                               products=auctioneer_profile_products,
                               title=title,
                               description=description,
                               session_id=self.session.session_id
                               )

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
        sessions = list(Session.objects.all().values('id', 'products', 'title',
                                                     'description', 'session_id'))

        return JsonResponse({'sessions':sessions})
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
