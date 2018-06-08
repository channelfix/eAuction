import axios from 'axios'

export default class Request {
	send(method = "get", url, data = {}, callback){
		axios({
			url: url,
			method: method,
			headers: {
				'X-Requested-With': 'XMLHttpRequest',
				"Access-Control-Allow-Methods": 'POST',
			},
			xsrfHeaderName: 'X-CSRFToken',
			xsrfCookieName: 'csrftoken',
			data: data, 			
		})
		.then((response)=>callback(response))
		.catch((error)=>callback(error))
	}

	post(url, data, callback){
		this.send('post', url, data, callback);
	}

	get(url, callback){
		this.send('get', url, {}, callback);
	}
}