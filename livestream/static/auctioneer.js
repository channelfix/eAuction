
// Display the session id and token of the auctioneer
console.log('Session ID: ' + sessionId);
console.log('Token: ' + token);

var session, publisher;
var hasPublish = false;

if(OT.checkSystemRequirements() == 1){ // Check if this browser supports WebRTC.
	console.log('This browser supports WebRTC.');
	session = OT.initSession(apiKey, sessionId);

	session.connect(token, function(error) { // Check if the client has successfully connected to the session.
		if(error)
			console.log('Cannot connect to the session.');
		else{
			console.log('Connected to the session.');

			// Create a publisher for exposing the video to other client who is also connected to the same session.
			publisher = OT.initPublisher('publisher', {insertMode: "append"}); 
			
			var btnStart = document.getElementById("1");
			var btnStop = document.getElementById("2");

			dispatchStartVideo(btnStart);
			dispatchEndVideo(btnStop);
		}
	});
}
else
	console.log('This browser does not support WebRTC.');


function dispatchStartVideo(btnStart) {

	// Dispatch for start auction
	btnStart.addEventListener("click", function() {

		if(!hasPublish){
			session.publish(publisher);
			alert('Starting to publish.');
			hasPublish = true;
		}
		else
			alert('On going streaming.');				
	});
}

function dispatchEndVideo(btnStop) {
	
	// Dispatch for end auction
	btnStop.addEventListener("click", function() {

		if(hasPublish){
			session.unpublish(publisher);
			alert('End the publish.');
			hasPublish = false;
			publisher = OT.initPublisher('publisher', {insertMode: "append"});
		}
		else
			alert('No publish has occured.');
	});
}
