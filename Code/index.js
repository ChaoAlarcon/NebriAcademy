const express = require("express")
const app = express();

let PORT = 4004; 

app.listen(PORT, ()=>{
    console.log(`App corriendo en el puerto ${PORT}...` )
})

// Landing page

app.get("/", (req,res)=>{
    res.send(`NebriAcademy ${JSON.stringify(req.params)}`)
})

// Login page

app.get("/login/", (req,res)=>{
    res.send(`Iniciar sesión o crear cuenta ${JSON.stringify(req.params)}`)
})

// Home page

app.get("/home/", (req,res)=>{
    res.send(`Bienvenido a tu home ${JSON.stringify(req.params)}`)
})

// Profile pages

app.get("/home/profile", (req,res)=>{
    res.send(`Mi perfil ${JSON.stringify(req.params)}`)
})

app.get("/home/profile/userdata", (req,res)=>{
    res.send(`Mis datos ${JSON.stringify(req.params)}`)
})

app.get("/home/profile/adjustments", (req,res)=>{
    res.send(`Ajustes ${JSON.stringify(req.params)}`)
})

// Saved Courses 

app.get("/home/savedcourses", (req,res)=>{
    res.send(`Mis cursos guardados ${JSON.stringify(req.params)}`)
})

// All Courses

app.get("/home/courses", (req,res)=>{
    res.send(`Todos los cursos ${JSON.stringify(req.params)}`)
})

app.get("/home/courses/titlepage/course/:courseId", (req,res)=>{
    res.send(`Presentación del curso ${JSON.stringify(req.params)}`)
})

app.get("/home/courses/learn/course/:courseId", (req,res)=>{
    res.send(`Aprende en el curso ${JSON.stringify(req.params)}`)
})

