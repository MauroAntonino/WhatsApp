class MessageService{
    constructor() {
        // var url = 'ws://localhost:3030'
        var url = urls.websocket_url
        var end_url = `${url}/?id=${user.id}`
        let ws = new WebSocket(end_url);
    
        ws.onopen = function() {
            console.log("Connected to Server"); 
        };
    
        ws.onclose = function() { 
            ws = null;
            alert("Connection closed... refresh to try again!"); 
        };
        this.ws = ws
    }

    send(msg) {
        this.ws.send(JSON.stringify(msg));
    }

    receive(cb){
        this.ws.onmessage = function ({data}) { 
            var msg = JSON.parse(data)
            cb(msg)
        };
    }
}