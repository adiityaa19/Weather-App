from multiprocessing import context
from django.shortcuts import render,redirect
from .form import CityForm
from .models import City
import requests
from django.contrib import messages

# Create your views here.

def index(request):
    template_name = 'index.html'
    context = {
        'title': 'Beranda',
    }
    return render(request, 'index.html', context)

def about(request):
    template_name = 'about.html'
    context = {
        'title': 'Kontak',
    }
    return render(request, 'about.html', context)

def weather(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={},&appid=6748d1bc82bfc3622a78e0a0759bf7e0&units=metric'

    if request.method=="POST":
        form=CityForm(request.POST)        
        if form.is_valid():
            NCity=form.cleaned_data['name']            
            CCity=City.objects.filter(name=NCity).count()
            if CCity==0:
                res=requests.get(url.format(NCity)).json()                
                if res['cod']==200:
                    form.save()
                    messages.success(request," "+NCity+" Added Successfully...!!!")
                else: 
                    messages.error(request,"City Does Not Exists...!!!")
            else:
                messages.error(request,"City Already Exists...!!!")      

    form=CityForm()
    cities=City.objects.all()
    data=[]
    for city in cities:        
        res=requests.get(url.format(city)).json()   
        city_weather={
            'city':city,
            'temperature' : res['main']['temp'],
            'description' : res['weather'][0]['description'],
            'country' : res['sys']['country'],
            'icon' : res['weather'][0]['icon'],
        }
        data.append(city_weather)  
    context={'data' : data,'form':form}
    return render(request, 'weatherapp.html', context)

def delete_city(request,CName):
    City.objects.get(name=CName).delete()
    messages.success(request," "+CName+" Removed Successfully...!!!")
    return redirect('weather')