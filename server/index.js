const WebSocket = require("ws");

const wss = new WebSocket.Server({ port: 3030 });

// wss.getUniqueID = function () {
//     function s4() {
//         return Math.floor((1 + Math.random()) * 0x10000).toString(16).substring(1);
//     }
//     return s4() + s4() + '-' + s4();
// };

var iter_users = (users, client) => {
    return new Promise((resolve, reject) => {
        users.forEach(function(value){
            if (value.id == client.id) {
                resolve(true)
            }
        })
        return false
    })
}

wss.on("connection", (ws, req) => {
    // ws.id = wss.getUniqueID();
    ws.id = req.url.replace('/?id=', '')
    console.log(`New client connected with id: ${ws.id}`);

    ws.onmessage = ({data}) => {
        var value = JSON.parse(data)
        console.log(`Client ${ws.id}: ${data}`);
        wss.clients.forEach(async function each(client) {
            var in_group = await iter_users(value['users'], client)
            if (in_group && client.readyState === WebSocket.OPEN && client !== ws) {
                client.send(`${data}`);
            }
        });
    };

    ws.onclose = function() {
        console.log(`Client ${ws.id} has disconnected!`);
    };
});
