import axios from 'axios'

export default class Request {
	send(method = "get", baseurl = "", url, data = {}, callback){
		axios({
			url: url,
			method: method,
			baseURL: baseurl,
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

	post(baseurl, url, data, callback){
		this.send('post',baseurl, url, data, callback);
	}

	get(baseurl, url, callback){
		this.send('get',baseurl, url, callback);
	}
}