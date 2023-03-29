# WhatsApp
>
> This project was ment to be a simple messaging app like Whatsapp. The messaging systems, the database, login service, the backend api are properly working as microservices, other fuctionalities can be added.
>
> Backend API is built with python, messaging is with websockets and login is built with javascript.
>
> That is an image captured of the app:
>
![Alt text](https://github.com/MauroAntonino/WhatsApp/blob/minimal/Screenshot_Whatsapp.png)
>
> To run the App is simple, just past the following commands in the terminal:
>
<pre><code>
sudo docker-compose build
</pre></code>
>
<pre><code>
sudo docker-compose up -d
</pre></code>
>
> to execute the app you have to build the database first, so execute the Tabela file with the sql commands in the MySql comandline.
>
> To create new groups, you can use the API for it.
>
>
> create group request example:
<pre><code>
{
	"name": "username",
	"password": "password",
	"group_name": "group_name",
	"description": "description"
}
</pre></code>
>
> add user group request example:
<pre><code>
{
	"name": "username",
	"password": "password",
	"group_name": "group_name"
}
</pre></code>
