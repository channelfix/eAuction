from django.shortcuts import render
from opentok import OpenTok, MediaModes, Roles, OutputModes
from .models import Session, Archive
from django.conf import settings
from django.http import HttpResponse
from django.views import View

# Static API attributes (TokBox Account)

# This class will create a unique session id for newly created session(room).
opentok_cloud = OpenTok(settings.OPENTOK_API_KEY,
                        settings.OPENTOK_API_SECRET)


class AuctionView(View):
    session_address = "127.0.0.1"
    # A session that gives more flexibility for more than two clients.
    session = opentok_cloud.create_session(session_address,
                                           media_mode=MediaModes.routed)

    # Check if there exist a session.
    if(not Session.objects.all()):
        # Store the new session id.
        sessions = Session(session_id=session.session_id)
        sessions.save()

    session_id = Session.objects.get(pk=1).session_id


# Main page (allows the user to choose between auctioneer and bidder).
def index(request):
    return render(request, 'video_stream/selection.html')

# This class will generate a token from
# the generated session id for the auctioneer.


class AuctioneerView(AuctionView):
    token = None
    context = {}

    def get(self, request):
        self.token = opentok_cloud.generate_token(self.session_id)
        self.context = {
            'api_key': settings.OPENTOK_API_KEY,
            'session_id': self.session_id,
            'token': self.token,
        }

        return render(request, 'video_stream/auctioneerPage.html',
                      self.context)


# This class will generate a token from
# the generated session id for the bidder.
class BidderView(AuctionView):

    token = None
    context = {}

    def get(self, request):
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
