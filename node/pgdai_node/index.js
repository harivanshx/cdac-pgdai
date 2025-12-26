// # this is a server application 


import express from "express";


const app = express();
const PORT = 3000;

// middleware to parse JSON
app.use(express.json());

// basic route
app.get("/", (req, res) => {
  res.send("Hello from Express!");
});

app.get("/api/getdata", (req, res) => {
  res.json({
    name:"harivansh",
    apple: "Brand Name",
    "pizza": "Dominos",
    
  });
});

// // example API route
// app.get("/api/health", (req, res) => {
//   res.json({ status: "OK" });
// });

// start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
