
console.log('Session ID: ' + sessionId);
console.log('Token: ' + token);


var session;
var xhttprequest;

var errorMessage = document.querySelector('h1'); // create a message when the stream is destroyed.
var successMessage = document.querySelector('h2'); // create a message when the stream is created.


if(OT.checkSystemRequirements() == 1){ // Check if this browser supports WebRTC.
	console.log('This browser supports WebRTC.');
	session = OT.initSession(apiKey, sessionId);

	session.connect(token, function(error) { // Check if this client is connected to the session.
		if(error)
			console.log('Cannot connect to the session.'); // Display Message: client has successfully connected to the session.
		else
			console.log('Connected to the session'); // Display Message: client has failed connect to the session.		
	});

	session.on("streamCreated", function(event) { // Check if the stream has created in a certain session.

		// Accept the exposed video who is connected to the same session.
		session.subscribe(event.stream, 'subscriber', {inserMode:'append', width:'50%', height:'50%'}); 
		console.log('Successfully subscribe');
		successMessage.textContent = 'Live';
		errorMessage.textContent = '';


		xhttprequest = new XMLHttpRequest();
		xhttprequest.onreadystatechange = function() {
			if(this.readyState == 4 && this.status == 200){
				alert(this.responseText);
			}
		}

		xhttprequest.open("GET", "/livestream/start_archive/", true); // Request for start recording the video.
		xhttprequest.send();	
	});


	session.on("streamDestroyed", function(event) {	

		xhttprequest = new XMLHttpRequest();
		xhttprequest.onreadystatechange = function() {
			if(this.readyState == 4 && this.status == 200){
				alert(this.responseText);
			}
		}

		xhttprequest.open("GET", "/livestream/end_archive/", true); // Request for stop recording the video.
		xhttprequest.send();


		console.log('Failed to subscribe');
		successMessage.textContent = '';
		errorMessage.textContent = 'No Auction event is available';
	});
}
else // Failed to launch the livestream.
	console.log('This browser does not support WebRTC.');