from django.shortcuts import render
from opentok import OpenTok, MediaModes, Roles, OutputModes
from .models import Session, Archive

from django.http import HttpResponse
from django.views import View

# Static API attributes (TokBox Account)
api_key = "46108532" 
api_secret = "e6d4e6a15044b30c45e55637c58eae77d7e84019"

# Static OpenTok cloud
opentok_cloud = OpenTok(api_key, api_secret)

session_address = "127.0.0.1" # Location of the server

# This class will create a unique session id for newly created session(room).
class AuctionView(View):		
	session = opentok_cloud.create_session(session_address, media_mode = MediaModes.routed) # A session that gives more flexibility for more than two clients.

	if(not Session.objects.all()): # Check if there exist a session.
		# Store the new session id.
	    sessions = Session(session_id = session.session_id) 
	    sessions.save()

	session_id = Session.objects.get(pk = 1).session_id


def index(request): # Main page (allows the user to choose between auctioneer and bidder).
    return render(request, 'video_stream/selection.html')


class AuctioneerView(AuctionView): # This class will generate a token from the generated session id for the auctioneer.

	token = None
	context = {}

	def get(self, request):

		self.token = opentok_cloud.generate_token(self.session_id)
		self.context = {
		    'api_key':api_key,
		    'session_id':self.session_id,
		    'token':self.token,
		}

		return render(request, 'video_stream/auctioneerPage.html', self.context)



class BidderView(AuctionView): # This class will generate a token from the generated session id for the bidder.

	token = None
	context = {}
	
	def get(self, request):

	    self.token = opentok_cloud.generate_token(self.session_id, role = Roles.subscriber)
	    self.context = {
	        'api_key':api_key,
	        'session_id':self.session_id,
	        'token':self.token,
	    } 
	    return render(request, 'video_stream/bidderPage.html', self.context)


def start_archive(request): # start to record the video.
    sessionId = Session.objects.get(pk=1).session_id

    archive = opentok_cloud.start_archive(sessionId, has_video=True, name='Test', output_mode=OutputModes.individual) # Start recording the video.
    archives = Archive(archive_id=archive.id)    
    archives.save()    

    return HttpResponse('Start recording')


def end_archive(request): # stop the video recording.
    archive_id = Archive.objects.get(pk=Archive.objects.count()).archive_id # get the id of the last archive object from Archive collections.
    opentok_cloud.stop_archive(archive_id) # Stop recording the video.
    return HttpResponse('Stop recording')

# Create your views here.
