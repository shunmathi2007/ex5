# Ex.05 Design a Website for Server Side Processing
## reference number:25012447
## Date:12.12.2025

## AIM:

To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

## FORMULA:

P = I2R

P --> Power (in watts)

 I --> Intensity
 
 R --> Resistance

## DESIGN STEPS:

### Step 1:

Clone the repository from GitHub.

### Step 2:

Create Django Admin project.

### Step 3:

Create a New App under the Django Admin project.

### Step 4:

Create python programs for views and urls to perform server side processing.

### Step 5:

Create a HTML file to implement form based input and output.

### Step 6:

Publish the website in the given URL.

## PROGRAM :
~~~
math.html
<!DOCTYPE html>
<html>
<head>
<title>Power Calculator</title>
<style>
    body{
        background:red;
        font-family:Arial;
    }
    .box{
        width:380px;
        padding:20px;
        margin:100px auto;
        background:blue;
        color:white;
        border:4px dotted green;
        text-align:center;
    }
    input{
        padding:5px;
        margin:5px;
        width:150px;
        text-align:center;
    }
</style>
</head>
<body>

<div class="box">
    <h2 style="color:pink;">Power of a Lamp</h2>

    <label>Current (I in Amps):</label><br>
    <input type="number" id="i"><br>

    <label>Resistance (R in Ohms):</label><br>
    <input type="number" id="r"><br>

    <button onclick="calcPower()">Calculate</button><br><br>

    <label>…
[11:43 am, 11/12/2025] shunmathi: from django.shortcuts import render

def mathpage(request):
    return render(request, 'mathapp/math.html')

    views.py
    from django.shortcuts import render
def mathpage(request):
    return render(request, 'mathapp/math.html')

urls.py
from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('math/',views.mathpage),

]
~~~


## SERVER SIDE PROCESSING:
![alt text](<ex05 power.png>)


## HOMEPAGE:
![alt text](<ex05 power 2.png>)

## RESULT:

The program for performing server side processing is completed successfully.


       
