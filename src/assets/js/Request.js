import axios from 'axios'
import Cookies from 'js-cookie'

export default class Request {
	send(method, baseurl, url, data){

		axios({
			url: url,
			method: method,
			baseURL: baseurl,
			// NOTE: do no do it like this 
			// headers: { 									
			// 	'X-CSRFToken': Cookies.get('csrftoken'),
			// 	'Access-Control-Allow-Origin': '*',
			// },
			headers: {
				'X-Requested-With': 'XMLHttpRequest'
			},
			xsrfHeaderName: 'X-CSRFToken',
			xsrfCookieName: 'csrftoken',
			data: JSON.stringify(data), //must stringify			
		})
		.then((response)=>{return response})
		.catch((error)=>{return error})
	}

	// must revise this part. POST and GET shouldn't expect same params
	post(baseurl, url, data){
		this.send('post',baseurl, url, data);
	}

	get(baseurl, url, data){
		this.send('get',baseurl, url, data);
	}
}