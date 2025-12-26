//   Create a new server and display a welcome message on browser 
import http from "http"
import os from "os"



const PORT = 3000;

// # we do use http . create server for creating your server 
// we do use req response for the requset ande resoponse 


const server = http.createServer((req, res) => {
  if (req.url === "/" && req.method === "GET") {
    res.write("<h1>Hello NODE JS FROM CDAC NOIDA </h1>");
  } 
  
  else {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Not Found");
  }
});

server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});


