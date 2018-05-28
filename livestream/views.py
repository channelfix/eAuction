from django.shortcuts import render
from opentok import OpenTok, MediaModes, Roles, OutputModes
from .models import Session, Archive
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'video_stream/selection.html')


class AuctioneerView(View):
    opentok_cloud = OpenTok(settings.OPENTOK_API_KEY,
                            settings.OPENTOK_API_SECRET)

    def getAuction(self):
        session_address = "127.0.0.1"
        session = self.opentok_cloud.create_session(
            session_address, media_mode=MediaModes.routed)

        sessions = Session.objects.create(
            session_id=session.session_id)
        session_id = session.session_id

        context = {
            'session_address': session_address,
            'opentok_cloud': session,
            'sessions': sessions,
            'session_id': session_id
        }

        return context

    def get(self, request, opentok_cloud):
        auction = self.getAuction()
        self.token = self.opentok_cloud.generate_token(auction['session_id'])
        self.context = {
            'api_key': settings.OPENTOK_API_KEY,
            'session_id': self.session_id,
            'token': self.token,
        }

        return JsonResponse(self.context)


# This class will generate a token from
# the generated session id for the bidder.
class BidderView(View):

    token = None
    context = {}

    def get(self, request, opentok_cloud):
        self.token = opentok_cloud.generate_token(self.session_id,
                                                  role=Roles.subscriber)
        self.context = {
            'api_key': settings.OPENTOK_API_KEY,
            'session_id': self.session_id,
            'token': self.token,
        }
        return render(request, 'video_stream/bidderPage.html', self.context)


# start to record the video.
def start_archive(request):
    sessionId = Session.objects.get(pk=1).session_id

    # Start recording the video.

    archive = opentok_cloud.start_archive(sessionId, has_video=True,
                                          name='Test',
                                          output_mode=OutputModes.individual)

    archives = Archive(archive_id=archive.id)
    archives.save()

    return HttpResponse('Start recording')


# stop the video recording.
def end_archive(request):
    # get the id of the last archive object from Archive collections.
    archive_id = Archive.objects.get(pk=Archive.objects.count()).archive_id
    # Stop recording the video.
    opentok_cloud.stop_archive(archive_id)

    return HttpResponse('Stop recording')

# Create your views here.
