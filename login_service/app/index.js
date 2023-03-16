const express = require('express');
const session = require('express-session');
const path = require('path');
const cookieParser = require('cookie-parser');
const Handlebars = require('handlebars');

const mysql_adapter = require('./adapters/mysql_adapter.js')
const User = require('./domain/repository/entities/users.js')
var fs = require('fs');

// console.log(__dirname)
// console.log(path.join(__dirname, 'static'))
// var chat_host = process.env.CHAT_HOST
var CHAT_URL = "http://localhost:3000/chat"
var AUTH_URL = "http://localhost:3000/"

// var CHAT_HTML = path.join(__dirname + '/static/index.html')
var CHAT_HTML = path.join(__dirname + '/static/zap/index_beta.html')
var SCRIPT_JS = path.join(__dirname + '/static/zap/script.js')
var DATE_JS = path.join(__dirname + '/static/zap/date-utils.js')
var DATA_JS = path.join(__dirname + '/static/zap/datastore.js')
var STYLE_JS = path.join(__dirname + '/static/zap/style.css')
var CHAT_HTML = path.join(__dirname + '/static/zap/index_beta.html')
var CHAT_HTML = path.join(__dirname + '/static/zap/index_beta.html')
var CHAT_HTML = path.join(__dirname + '/static/zap/index_beta.html')
var LOGIN_HTML = path.join(__dirname + '/static/login.html')
var SIGNIN_HTML = path.join(__dirname + '/static/signin.html')

const app = express();

app.use('/script', express.static(SCRIPT_JS));
app.use('/date', express.static(DATE_JS));
app.use('/data', express.static(DATA_JS));
app.use('/css',express.static(STYLE_JS));

app.use(session({
	secret: 'secret',
	resave: true,
	saveUninitialized: true
}));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
// app.use(express.static(path.join(__dirname, 'static')));
app.use(cookieParser());

// http://localhost:3000/
app.get('/', function(request, response) {
	// Render login template
	response.sendFile(LOGIN_HTML);
});

app.get('/create_user', function(request, response) {
	// Render login template
	response.sendFile(SIGNIN_HTML);
});

app.post('/login', async function(request, response) {
	let username = request.body.username;
	let password = request.body.password;
	var user = new User("", username, password, "")
	var adapter = new mysql_adapter()
	var results = await adapter.getUser(user)
	var error = results[0]
	results = results[1]
	if (error) {
		response.redirect(AUTH_URL)
	}
	else {
		request.session.loggedin = true;
		request.session.username = username;
		request.session.user_id = results.id;
		request.session.password = password
		response.redirect(CHAT_URL)
	}
});

app.post('/sign', async function(request, response) {
	let username = request.body.username;
	let password = request.body.password;
	let email = request.body.email;
	// let x = Math.random() * 100;
	var adapter = new mysql_adapter()
	var user = new User("", username, password, email)
	var values = await  adapter.saveUser(user)
	var error =values[0]
	var id =values[1]
	if(error) {
		response.redirect(AUTH_URL)
	}
	// connection.query(`INSERT INTO users (id, username, password, email) VALUES(1, '${username}', '${password}', '${email}') 
	// 					ON DUPLICATE KEY UPDATE username='${username}', password='${password}', email='${email}';`)
	request.session.loggedin = true;
	request.session.username = username;
	request.session.user_id = id;
	request.session.password = password
	response.redirect(CHAT_URL)
});

app.get('/chat', async function(request, response){
	if (request.session.loggedin){
		var err, words = await fs.promises.readFile(CHAT_HTML, 'utf8');
		var template = Handlebars.compile(words);
		console.log({"name": request.session.username, "id": request.session.user_id, "password": request.session.password})
		data = {"name": request.session.username, "id": request.session.user_id, "password": request.session.password}
		var result = template(data);
		response.send(result)
	}
	else{
		response.redirect(AUTH_URL)
	}
})

app.post('/logout', async function(request, response){
	if (request.session.loggedin){
		request.session.loggedin = false
		response.redirect(AUTH_URL)
	}
	else{
		response.redirect(AUTH_URL)
	}
})

app.listen(3000, ()=> {
    console.log("server started on port 3000")
})