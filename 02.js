const express = require("express");
const session = require("express-session");
const bodyParser = require("body-parser");

const app = express();
const PORT = 3000;

app.use(bodyParser.urlencoded({ extended: true }));

app.use(
    session({
        secret: "your-secret-key",
        resave: false,
        saveUninitialized: true
    })
);

// Serve static files
app.use(express.static("public"));

// Login route
app.post("/save", (req, res) => {
    const { username, password } = req.body;
    req.session.username = username;
    req.session.password = password;
    res.redirect("/fetchdata");
});

// Authentication route
app.get("/fetchdata", (req, res) => {
    if (req.session.username === "admin" && req.session.password === "admin@123") {
        res.send(`<h2>Welcome, Admin!</h2><a href='/logout'>Logout</a>`);
    } else {
        res.send(`<h2>Invalid credentials!</h2><a href='/'>Go Back</a>`);
    }
});

// Logout route
app.get("/logout", (req, res) => {
    req.session.destroy();
    res.redirect("/");
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
