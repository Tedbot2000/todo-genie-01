from django.shortcuts import render 
from django.views.generic import TemplateView 
class HomePage(TemplateView): 
""" 
Displays home page" 
""" 
template_name = 'index.html' 

In templates folder index.html

{% load static %}

<!DOCTYPE html> 
<html lang="en"> 
<head> 
<meta charset="UTF-8"> 
<meta name="viewport" 
content="width=device-width, initial-scale=1.0"> 
<title>Django-Setup</title> 
<link rel="stylesheet" href="{% static 'css/style.css' %}"> 
</head> 
<body> 
<h1>Hello Django From Heroku</h1> 
</body> 
</html>