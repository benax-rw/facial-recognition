const http = require("http");
const WebSocket = require("ws"); // Import the WebSocket library
const fs = require("fs"); // Import the File System module

const port = 3033;

const server = http.createServer((req, res) => {
    if (req.method === "POST") {
        let body = "";
        req.on("data", (data) => {
            body += data;
        });
        req.on("end", () => {
            console.log("Received data from sketch.js:", body);
            // Broadcast data to all connected clients
            wss.clients.forEach((client) => {
                if (client.readyState === WebSocket.OPEN) {
                    client.send(body);
                }
            });

            res.end("Data received");
        });
    } else {
        res.end("Invalid request");
    }
});

const wss = new WebSocket.Server({ server }); // Create a WebSocket server

wss.on("connection", (socket) => {
    console.log("WebSocket connection established");

    socket.on("message", (data) => {
        console.log("Received data from sketch.js:", data);

        // Broadcast data to all connected clients
        wss.clients.forEach((client) => {
            if (client !== socket && client.readyState === WebSocket.OPEN) {
                client.send(data);
            }
        });
    });
});

server.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
