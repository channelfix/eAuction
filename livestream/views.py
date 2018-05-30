from django.shortcuts import render
from opentok import OpenTok, MediaModes, Roles, OutputModes
from .models import Session, Archive
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views import View


class OpenTokCloudView(View):
    opentok_cloud = OpenTok(settings.OPENTOK_API_KEY,
                            settings.OPENTOK_API_SECRET)

    def get_cloud(self):
        return self.opentok_cloud


class AuctioneerView(OpenTokCloudView):
    session_id = ''
    token = ''

    def get_auction(self):
        """ Create an Auction Event """

        opentok_cloud = super(AuctioneerView, self).get_cloud()
        session_address = "127.0.0.1"
        session = opentok_cloud.create_session(session_address,
                                                    media_mode=MediaModes.routed)

        # Store the new session id
        Session.objects.create(session_id=session.session_id)
        self.session_id = session.session_id

        return {'session_id': self.session_id}

    def set_session_id(self):

        # Hard coded
        self.session_id = Session.objects.get(pk=Session.objects.count()).session_id

    def get_session_id(self):
        return self.session_id

    def get(self, request):
        auction = self.get_auction()
        self.session_id = auction['session_id']
        self.token = self.opentok_cloud.generate_token(self.session_id)

        context = {
            'api_key': settings.OPENTOK_API_KEY,
            'session_id': self.session_id,
            'token': self.token,
        }

        return JsonResponse(context)


# This class will generate a token from
# the generated session id for the bidder.
class BidderView(AuctioneerView):
    token = ''

    def get(self, request):
        auctioneer_view = super(BidderView, self)
        auctioneer_view.set_session_id()
        session_id = auctioneer_view.get_session_id()
        self.token = auctioneer_view.get_cloud().generate_token(session_id,
                                                                role=Roles.subscriber)
        context = {
            'api_key': settings.OPENTOK_API_KEY,
            'session_id': session_id,
            'token': self.token,
        }

        return JsonResponse(context)


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

# Create your views here.
