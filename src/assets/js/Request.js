import axios from 'axios'
import Cookies from 'js-cookie'

export default class Request {
	send(method, baseurl, url, data){
		axios({
			url: url,
			method: method,
			baseURL: baseurl,
			headers: {
				'X-CSRFToken': Cookies.get('csrftoken')
			},
			data: data,
		})
		.then((response)=>{return response})
		.catch((error)=>{return error})
	}

	post(baseurl, url, data){
		this.send('post',baseurl, url, data);
	}

	get(baseurl, url, data){
		this.send('get',baseurl, url, data);
	}
}