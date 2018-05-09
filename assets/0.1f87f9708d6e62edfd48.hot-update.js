webpackHotUpdate(0,{

/***/ "./src/assets/js/Request.js":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_axios__ = __webpack_require__(\"./node_modules/axios/index.js\");\n/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_axios___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_axios__);\n/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_js_cookie__ = __webpack_require__(\"./node_modules/js-cookie/src/js.cookie.js\");\n/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_js_cookie___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_js_cookie__);\n\n\n\nclass Request {\n\tsend(method, baseurl, url, data) {\n\n\t\t__WEBPACK_IMPORTED_MODULE_0_axios___default()({\n\t\t\turl: url,\n\t\t\tmethod: method,\n\t\t\tbaseURL: baseurl,\n\t\t\t// NOTE: do no do it like this \n\t\t\t// headers: { \t\t\t\t\t\t\t\t\t\n\t\t\t// \t'X-CSRFToken': Cookies.get('csrftoken'),\n\t\t\t// \t'Access-Control-Allow-Origin': '*',\n\t\t\t// },\n\t\t\theaders: {\n\t\t\t\t'X-Requested-With': 'XMLHttpRequest'\n\t\t\t},\n\t\t\txsrfHeaderName: 'X-CSRFToken',\n\t\t\txsrfCookieName: 'csrftoken',\n\t\t\tdata: data //must stringify\t\t\t\n\t\t}).then(response => {\n\t\t\treturn response;\n\t\t}).catch(error => {\n\t\t\treturn error;\n\t\t});\n\t}\n\n\t// must revise this part. POST and GET shouldn't expect same params\n\tpost(baseurl, url, data) {\n\t\tconsole.log(data);\n\t\tthis.send('post', baseurl, url, data);\n\t}\n\n\tget(baseurl, url, data) {\n\t\tthis.send('get', baseurl, url, data);\n\t}\n}\n/* harmony export (immutable) */ __webpack_exports__[\"a\"] = Request;\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvYXNzZXRzL2pzL1JlcXVlc3QuanMuanMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8vc3JjL2Fzc2V0cy9qcy9SZXF1ZXN0LmpzPzA1MDMiXSwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IGF4aW9zIGZyb20gJ2F4aW9zJ1xuaW1wb3J0IENvb2tpZXMgZnJvbSAnanMtY29va2llJ1xuXG5leHBvcnQgZGVmYXVsdCBjbGFzcyBSZXF1ZXN0IHtcblx0c2VuZChtZXRob2QsIGJhc2V1cmwsIHVybCwgZGF0YSl7XG5cblx0XHRheGlvcyh7XG5cdFx0XHR1cmw6IHVybCxcblx0XHRcdG1ldGhvZDogbWV0aG9kLFxuXHRcdFx0YmFzZVVSTDogYmFzZXVybCxcblx0XHRcdC8vIE5PVEU6IGRvIG5vIGRvIGl0IGxpa2UgdGhpcyBcblx0XHRcdC8vIGhlYWRlcnM6IHsgXHRcdFx0XHRcdFx0XHRcdFx0XG5cdFx0XHQvLyBcdCdYLUNTUkZUb2tlbic6IENvb2tpZXMuZ2V0KCdjc3JmdG9rZW4nKSxcblx0XHRcdC8vIFx0J0FjY2Vzcy1Db250cm9sLUFsbG93LU9yaWdpbic6ICcqJyxcblx0XHRcdC8vIH0sXG5cdFx0XHRoZWFkZXJzOiB7XG5cdFx0XHRcdCdYLVJlcXVlc3RlZC1XaXRoJzogJ1hNTEh0dHBSZXF1ZXN0J1xuXHRcdFx0fSxcblx0XHRcdHhzcmZIZWFkZXJOYW1lOiAnWC1DU1JGVG9rZW4nLFxuXHRcdFx0eHNyZkNvb2tpZU5hbWU6ICdjc3JmdG9rZW4nLFxuXHRcdFx0ZGF0YTpkYXRhLCAvL211c3Qgc3RyaW5naWZ5XHRcdFx0XG5cdFx0fSlcblx0XHQudGhlbigocmVzcG9uc2UpPT57cmV0dXJuIHJlc3BvbnNlfSlcblx0XHQuY2F0Y2goKGVycm9yKT0+e3JldHVybiBlcnJvcn0pXG5cdH1cblxuXHQvLyBtdXN0IHJldmlzZSB0aGlzIHBhcnQuIFBPU1QgYW5kIEdFVCBzaG91bGRuJ3QgZXhwZWN0IHNhbWUgcGFyYW1zXG5cdHBvc3QoYmFzZXVybCwgdXJsLCBkYXRhKXtcblx0XHRjb25zb2xlLmxvZyhkYXRhKVxuXHRcdHRoaXMuc2VuZCgncG9zdCcsYmFzZXVybCwgdXJsLCBkYXRhKTtcblx0fVxuXG5cdGdldChiYXNldXJsLCB1cmwsIGRhdGEpe1xuXHRcdHRoaXMuc2VuZCgnZ2V0JyxiYXNldXJsLCB1cmwsIGRhdGEpO1xuXHR9XG59XG5cblxuLy8gV0VCUEFDSyBGT09URVIgLy9cbi8vIHNyYy9hc3NldHMvanMvUmVxdWVzdC5qcyJdLCJtYXBwaW5ncyI6IkFBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBREE7QUFHQTtBQUNBO0FBQ0E7QUFkQTtBQWdCQTtBQUFBO0FBQ0E7QUFBQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUEvQkE7OyIsInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./src/assets/js/Request.js\n");

/***/ })

})