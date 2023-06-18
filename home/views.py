from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
import time
import uuid
from django.core.mail import *
from django.template.loader import *
from django.utils import *
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.http import urlencode
from django.views.decorators.csrf import csrf_exempt
import folium
from django.utils import timezone
import pytz
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/account/login')
    else:
        userid = request.user.id
        if request.user.is_superuser:
            device = deviced.objects.all().values("device_id",'id')
        else:
            device = deviced.objects.filter(user=userid).values("device_id",'id')
        userc = User.objects.count()
        usercactive = User.objects.filter(is_active=True).count()
        devicec = deviced.objects.count()
        deviceconline = deviced.objects.filter(is_online=True).count()
            # create map object
        mymap = folium.Map(location=[23.603605, 79.255619], zoom_start=4)
        # set tiles to "Stamen Terrain" or "Stamen Toner" to display a plain background
        folium.TileLayer(tiles='Stamen Terrain', name='Terrain', show=True).add_to(mymap)
        
    # add marker to the map
        folium.Marker(location=[28.632811, 77.211565], popup='London').add_to(mymap)
        
        context = {'device': device,'usercactive':usercactive,'userc':userc,'devicec':devicec,'deviceconline':deviceconline,'map':mymap._repr_html_()}
        return render(request, 'index.html', context)



def adddevice(request):
    if not request.user.is_authenticated:
        return redirect('/account/login')
    else:
        if request.method == 'POST':
    
            userid = request.POST['userid']
            deviceid = request.POST['deviceid']
            vehicle_name = request.POST['vehiclename']
            vehicle_number = request.POST['vehiclenumber']
            users = User.objects.get(id=userid)

           
            device = deviced.objects.create(user=users,device_id=deviceid,vehicle_name=vehicle_name,vehicle_number=vehicle_number)
            
            device.save()
            sensordevice = SensorData.objects.create(device=device)
            sensordevice.save()
            messages.success(request, 'Device Added')
            return redirect('device_details')
        else:
            userall = User.objects.all()
            context = {'userdata': userall}
            return render(request, 'adddevicedetails.html', context)


def device_details(request):
    if not request.user.is_authenticated:
        return redirect('/account/login')
    else:
        if request.user.is_superuser:
            device = deviced.objects.all()
            userall = User.objects.all()
            context = {'devices': device,'user': userall}
            return render(request, 'devices.html', context)  
        userid = request.user.id
        device = deviced.objects.filter(user=userid)
        userall = User.objects.all()
        context = {'devices': device,'user': userall}
        
        return render(request, 'devices.html', context)
    

def delete_device(request, pk):
    if not request.user.is_authenticated:
        return redirect('/account/login')
    else:
        device = deviced.objects.get(pk=pk)
        device.delete()
        messages.error(request, 'Device Deleted')
        return redirect('device_details')
    
def edit_device(request,device_id=None):
    if not request.user.is_authenticated:
        return redirect('/account/login')
    else:
        if device_id:
            if request.method == 'POST':
                device = deviced.objects.get(id=device_id)
                device.user = User.objects.get(id=request.POST['userid'])
                device.device_id = request.POST['deviceid']
                device.vehicle_name = request.POST['vehiclename']
                device.vehicle_number = request.POST['vehiclenumber']
                device.is_online = request.POST['is_online']
                device.save()
                device = deviced.objects.get(device_id=request.POST['deviceid'])
                sensordevice = SensorData.objects.create(device=device)
                sensordevice.save()
                messages.info(request,"Data Updated")
                return redirect('device_details')
            else:
                userall = User.objects.all()
                context = {'userdata': userall, 'device': device}
                return render(request, 'adddevicedetails.html', context)
        else:
            messages.error(request,"Device Id or Device Not Found")
            return redirect('device_details')


def adduser(request):
    if not request.user.is_authenticated:
            return redirect('/account/login')
    else:
        if request.method == 'POST':
                first_name = request.POST['fname']
                last_name = request.POST['lname']
                username = request.POST['uname']
                password1 = request.POST['password1']
                password2 = request.POST['password2']
                email = request.POST['email']

                if password1 == password2:
                    if User.objects.filter(username=username).exists():
                        messages.info(request, 'Username Taken')
                        print('user exits')
                    elif User.objects.filter(email=email).exists():
                        messages.info(request, 'Email Taken')
                    else:
                        user = User.objects.create_user(username=username, password=password1, email=email,
                                                        first_name=first_name, last_name=last_name)
                        user.save();
                        messages.success(request, 'user created')
                        print('user created')
                        return redirect('/userlist')

                else:
                    messages.info(request, 'password not matching..')
        
        return render(request, 'adduser.html')
    
def user_details(request):
    if not request.user.is_authenticated:
        return redirect('/account/login')
    else:
        userall = User.objects.all()
        for userd in userall:
            userd.first_name = userd.first_name
            userd.last_name = userd.last_name
            userd.username = userd.username
            userd.email  = userd.email
            userd.is_active = userd.is_active
            userd.date_joined = userd.date_joined
            userd.last_login = userd.last_login
            userd.is_superuser = userd.is_superuser
            
        context = {'user': userall}
        
        return render(request, 'users.html', context)
    
def edit_user(request,id=None):
    if not request.user.is_authenticated:
        return redirect('/account/login')
    else:
        if id:
            if request.method == 'POST':
                first_name = request.POST['fname']
                last_name = request.POST['lname']
                username = request.POST['uname']
                password1 = request.POST['password1']
                password2 = request.POST['password2']
                email = request.POST['email']
                is_active = request.POST['is_active']
                if password1 == password2:
                    user = User.objects.get(id=id)
                    if user.password == password1:
                        user.first_name = first_name
                        user.last_name =last_name
                        user.username = username
                        user.email = email
                        # change the is_active field
                        user.is_active= is_active
                        user.save();
                        messages.success(request, 'DATA pass UPDATED')
                        return redirect('/userlist')
                    else:
                        user.first_name = first_name
                        user.last_name =last_name
                        user.username = username
                        user.email = email
                        user.set_password(password1)
                        # change the is_active field
                        user.is_active= is_active
                        user.save();
                        messages.success(request, 'DATA  UPDATED')
                        return redirect('/userlist')
                else:
                    messages.success(request, 'Password Didnt match')
                    return redirect('/userlist')
            else:
                userall = User.objects.all()
                context = {'user': userall}
                return render(request, 'users.html', context)
        else:
            messages.error(request,"Device Id or Device Not Found")
            return redirect('userlist')
        
def delete_user(request, pk):
    if not request.user.is_authenticated:
        return redirect('/account/login')
    else:
        user = User.objects.get(pk=pk)
        user.delete()
        messages.error(request, 'Device Deleted')
        return redirect('userlist')
    
    
def store_data(request):
    deviceid =request.GET.get('deviceid')
    vibration = request.GET.get('vibration')
    gaslink = request.GET.get('gaslink')
    temperaturea = request.GET.get('t')
    temperatured = request.GET.get('tempd')
    humidity = request.GET.get('h')
    fangle = request.GET.get('fangle')
    voltage = request.GET.get('voltage')
    
    # set the timezone for India
    india_tz = pytz.timezone('Asia/Kolkata')

    # get the current datetime in UTC
    utc_datetime = timezone.now()

    # convert the datetime to India timezone
    india_datetime = utc_datetime.astimezone(india_tz)

    # set the time field to the current date and time in India timezone

    time_field = india_datetime
    deviceds = deviced.objects.get(device_id = deviceid)
    deviceds.is_online=True
    sensordata = SensorData.objects.create(device_id = deviceds.id,vibration=vibration,gaslink=gaslink, temperaturea=temperaturea,temperatured=temperatured,humidity=humidity,fangle =fangle, voltage = voltage,timed = time_field)
    deviceds.save()
    sensordata.save()

    # Store data in database
    ...

    return HttpResponse('Data stored')


@csrf_exempt
def selectvibdata(request,device_id):
    
    sensordata = SensorData.objects.filter(device=device_id).order_by('-timed')[:10].values('vibration','timed')

    for item in sensordata:
        item['vibration'] =item['vibration']
        item['timed'] = item['timed'].astimezone(timezone.get_current_timezone())
        item['timed'] = item['timed'].strftime('%y-%m-%d - %H:%M')
        
    return JsonResponse(list(sensordata), safe=False)

def selectgasdata(request,device_id):
    
    sensordata = SensorData.objects.filter(device=device_id).order_by('-timed')[:10].values('gaslink','timed')

    for item in sensordata:
        item['gaslink'] =item['gaslink']
        item['timed'] = item['timed'].astimezone(timezone.get_current_timezone())
        item['timed'] = item['timed'].strftime('%y-%m-%d - %H:%M')
        
    return JsonResponse(list(sensordata), safe=False)


def selecttempadata(request,device_id):
    
    sensordata = SensorData.objects.filter(device=device_id).order_by('-timed')[:10].values('temperaturea','timed')

    for item in sensordata:
        item['temperaturea'] =item['temperaturea']
        item['timed'] = item['timed'].astimezone(timezone.get_current_timezone())
        item['timed'] = item['timed'].strftime('%y-%m-%d - %H:%M')
        
    return JsonResponse(list(sensordata), safe=False)

def selecthumiditydata(request,device_id):
    
    sensordata = SensorData.objects.filter(device=device_id).order_by('-timed')[:10].values('humidity','timed')

    for item in sensordata:
        item['humidity'] =item['humidity']
        item['timed'] = item['timed'].astimezone(timezone.get_current_timezone())
        item['timed'] = item['timed'].strftime('%y-%m-%d - %H:%M')
        
    return JsonResponse(list(sensordata), safe=False)


def selectflexangledata(request,device_id):
    
    sensordata = SensorData.objects.filter(device=device_id).order_by('-timed')[:10].values('fangle','timed')

    for item in sensordata:
        item['fangle'] =item['fangle']
        item['timed'] = item['timed'].astimezone(timezone.get_current_timezone())
        item['timed'] = item['timed'].strftime('%y-%m-%d - %H:%M')
        
    return JsonResponse(list(sensordata), safe=False)


def selectvoldata(request,device_id):
    
    sensordata = SensorData.objects.filter(device=device_id).order_by('-timed')[:10].values('voltage','timed')

    for item in sensordata:
        item['voltage'] =item['voltage']
        item['timed'] = item['timed'].astimezone(timezone.get_current_timezone())
        item['timed'] = item['timed'].strftime('%y-%m-%d - %H:%M')
        
    return JsonResponse(list(sensordata), safe=False)




def selecttempddata(request,device_id):
    
    sensordata = SensorData.objects.filter(device=device_id).order_by('-timed')[:10].values('temperatured','timed')

    for item in sensordata:
        item['temperatured'] =item['temperatured']
        item['timed'] = item['timed'].astimezone(timezone.get_current_timezone())
        item['timed'] = item['timed'].strftime('%y-%m-%d - %H:%M')
        
    return JsonResponse(list(sensordata), safe=False)