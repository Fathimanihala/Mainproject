from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from MyApp.models import *


def login(request):
    return render(request,"loginindex.html")


def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    l=Login.objects.filter(username=username,password=password)
    if l.exists():
        r=Login.objects.get(username=username,password=password)
        request.session['lid']=r.id
        if r.type == "admin":
            return  HttpResponse('''<script>alert("welcom");window.location='/myapp/adminhomepage/'</script>''')
    return HttpResponse('''<script>alert("Invalid User Not Found");window.location='/myapp/login/'</script>''')

def changepass(request):
    return render(request,"changepassword.html")
def changepass_post(request):
    Currenpassword=request.POST['textfield']
    Newpassword=request.POST['textfield2']
    Confirmpassword=request.POST['textfield3']
    p=Login.objects.filter(id=request.session['lid'],password=Currenpassword)
    if p.exists():
        if Newpassword==Confirmpassword:
            c=Login.objects.filter(id=request.session['lid'],password=Currenpassword).update(password=Newpassword)
            return HttpResponse('''<script>alert("Password Updated");window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("Password Does Not Match");window.location='/myapp/changepass/'</script>''')
    else:
        return HttpResponse('''<script>alert("User Not Found");window.location='/myapp/changepass/'</script>''')

def routeadds(request):
    return render(request, "routeadd.html")

def routeadds_post(request):
    Routename=request.POST['textfield']
    FromPlace=request.POST['textfield2']
    Toplace=request.POST['textfield3']
    r=Route()
    r.routename=Routename
    r.fromplace=FromPlace
    r.toplace=Toplace
    r.save()
    return HttpResponse('''<script>alert("Added");window.location='/myapp/routeadds/'</script>''')
def routeedits(request,id):
    v=Route.objects.get(id=id)
    return render(request, "routeedit.html",{'data':v})
def routeedits_post(request):
    id=request.POST['id']
    Routename = request.POST['textfield']
    FromPlace = request.POST['textfield2']
    Toplace = request.POST['textfield3']
    rou=Route.objects.get(id=id)
    rou.routename = Routename
    rou.fromplace = FromPlace
    rou.toplace = Toplace
    rou.save()
    return HttpResponse('''<script>alert("Edited Successfully");window.location='/myapp/routeviews/'</script>''')


def routedelete(request,id):
    g=Route.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("Deleted Successfully");window.location='/myapp/routeviews/'</script>''')
.def routeviews(request):
    v=Route.objects.all()
    return render(request, "routeview.html",{'data':v})


def busadds(request):
    b=Route.objects.all()
    return render(request, "busadd.html",{'data':b})
def busadds_post(request):
    Busregno=request.POST['textfield5']
    Busmodel=request.POST['textfield4']
    chasisnumber=request.POST['textfield3']
    manufacturename=request.POST['textfield2']
    r=request.POST['select']
    obj=Bus()
    obj.busregno=Busregno
    obj.busmodel=Busmodel
    obj.chasisnumber=chasisnumber
    obj.manufacturename=manufacturename
    obj.ROUTE_id=r
    obj.save()
    return HttpResponse('''<script>alert("Added Successfully");window.location='/myapp/busadds/'</script>''')
def driveadds(request):
    b=Route.objects.all()
    return render(request, "add drive.html",{'data':b})
def driveadds_post(request):
    name=request.POST['textfield5']
    email=request.POST['textfield4']
    phone=request.POST['textfield3']
    image=request.FILES['textfi']
    l=Login()
    l.username=email
    l.password=phone
    l.type='driver'
    l.save()

    obj=Driver()
    obj.name=name
    obj.email=email
    obj.phone=phone
    fs = FileSystemStorage()
    date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fs.save(date, image)
    path = fs.url(date)
    obj.image=path
    obj.LOGIN=l
    obj.save()
    return HttpResponse('''<script>alert("Added Successfully");window.location='/myapp/driveadds/'</script>''')
def driveallocate(request):
    b=Bus.objects.all()
    d=Driver.objects.all()
    return render(request, "allocatebus.html",{'data1':b,'data':d})
def driveallocate_post(request):
    drive=request.POST['select']
    bus=request.POST['select1']

    obj=Allocate()
    obj.DRIVER_id=drive
    obj.BUS_id=bus
    obj.save()
    return HttpResponse('''<script>alert("Added Successfully");window.location='/myapp/driveallocate/'</script>''')

def driveedit(request,id):
    b=Driver.objects.get(id=id)
    return render(request, "driveedit.html",{'data':b})
def driveedit_post(request):
    name=request.POST['textfield5']
    email=request.POST['textfield4']
    phone=request.POST['textfield3']
    id=request.POST['id']
    l=Login.objects.get(id=id)
    l.username=email
    l.save()

    obj=Driver.objects.get(LOGIN_id=id)

    if 'textfi' in request.FILES:
        image=request.FILES['textfi']
        fs = FileSystemStorage()
        date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs.save(date, image)
        path = fs.url(date)
        obj.image=path
        obj.save()
    obj.name = name
    obj.email = email
    obj.phone = phone
    obj.save()
    return HttpResponse('''<script>alert("Edited Successfully");window.location='/myapp/driveviews/'</script>''')



def busviews(request):
    v=Bus.objects.all()
    return render(request, "busview.html",{'data':v})
def allocateviews(request):
    v=Allocate.objects.all()
    return render(request, "allocateview.html",{'data':v})

def driveviews(request):
    v=Driver.objects.all()
    return render(request, "driveview.html",{'data':v})


def busedits(request,id):
    v=Route.objects.all()
    D=Bus.objects.get(id=id)
    return render(request,"busedit.html",{'data':D,'data1':v})

def busedits_post(request):
    id = request.POST['id']
    Busregno = request.POST['textfield5']
    Busmodel = request.POST['textfield4']
    chasisnumber = request.POST['textfield3']
    manufacturename = request.POST['textfield2']
    r = request.POST['select']
    obj=Bus.objects.get(id=id)
    obj.busregno=Busregno
    obj.busmodel=Busmodel
    obj.chasisnumber=chasisnumber
    obj.manufacturename=manufacturename
    obj.ROUTE_id=r
    obj.save()
    return HttpResponse('''<script>alert("Edited Successfully");window.location='/myapp/busview/'</script>''')


def busdelete(request,id):
    delt=Bus.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert("Deleted Successfully");window.location='/myapp/busview/'</script>''')
def allodelete(request,id):
    delt=Allocate.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert("Deleted Successfully");window.location='/myapp/allocateviews/'</script>''')

def drivedelete(request,id):
    delt=Driver.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("Deleted Successfully");window.location='/myapp/driveviews/'</script>''')



def busstopadds(request):
    res=Route.objects.all()
    return render(request, "busstopadd.html",{'data':res})

def busstopadds_post(request):
    route=request.POST['textfield']
    placename=request.POST['textfield2']
    longitude=request.POST['textfield4']
    latitude=request.POST['textfield3']
    opt=Busstop()
    opt.placename=placename
    opt.longitude=longitude
    opt.latitude=latitude
    opt.ROUTE=Route.objects.get(id=route)
    opt.save()
    return HttpResponse('''<script>alert("busstop Added");window.location='/myapp/busstopadds/'</script>''')

def busstopviews(request):
    st = Busstop.objects.all()
    return render(request, "busstopview.html",{'data':st})

def busstopdelete(request,id):
    dele=Busstop.objects.filter(id=id).delete()
    return redirect('/myapp/busstopviews/')

def busstopedits(request,id):
    e = Route.objects.all()
    us = Busstop.objects.get(id=id)
    return render(request,"busstopedit.html" ,{'data':e,'data1':us})

def busstopedits_post(request):
    id=request.POST['id']
    placename = request.POST['textfield2']
    longitude = request.POST['textfield4']
    latitude = request.POST['textfield3']
    re = request.POST['textfield']
    ob = Busstop.objects.get(id=id)
    ob.placename = placename
    ob.longitude = longitude
    ob.latitude = latitude
    ob.ROUTE_id = re
    ob.save()
    return HttpResponse('''<script>alert("busstop Edited");window.location='/myapp/busstopviews/'</script>''')





def locations(request):
    res=Location.objects.all()
    return render(request,"location.html",{"data":res})


def notification(request):
    return render(request,"notification.html")
def notification_post(request):
    notification = request.POST['textfield']
    emg = Notification()
    emg.notification = notification
    from datetime import datetime
    date = datetime.now().date().today()
    emg.date = date
    emg.save()
    return HttpResponse('''<script>alert("notification");window.location='/myapp/notification/'</script>''')


def adminnviewnotification(request):
    v=Notification.objects.all()
    return render(request,'viewadminnotification.html',{'data':v})

def notificationdelete(request,id):
    deel=Notification.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert("Msg Delete");window.location='/myapp/adminnviewnotification/'</script>''')


def emergencynotify(request):
    return render(request,"emergency notification.html")

def emergencynotify_post(request):
    notification=request.POST['textfield']
    emg=EmergencyNotification()
    emg.notification=notification
    from datetime import datetime
    date=datetime.now().date().today()
    emg.date=date
    emg.save()
    return HttpResponse('''<script>alert("Emergency Alert");window.location='/myapp/emergencynotify/'</script>''')

def adminnewemergencynotification(request):
    v=EmergencyNotification.objects.all()
    return render(request,'viewemergencynotification.html',{'data':v})

def emergencynotificationdelete(request,id):
    dell=EmergencyNotification.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert("Emergency msg Delete");window.location='/myapp/adminnewemergencynotification/'</script>''')

def user(request):
    u=User.objects.all()
    return render(request,"userview.html",{'data':u})

def searchuser(request):
    s=request.POST['textfield']
    u=User.objects.filter(name__icontains=s)
    return render(request,"userview.html",{'data':u})

def adminhomepage(request):
    return render(request,"homeindex.html")





# --------------------------------------------------------user---------------------------------------


def registration(request):
    name=request.POST['name']
    phoneno = request.POST['phoneno']
    email = request.POST['email']
    place = request.POST['place']
    post = request.POST['post']
    pincode =request.POST['pincode']
    district =request.POST['district']
    idproof=request.POST['idproof']
    password=request.POST['password']
    conformpassword=request.POST['conformpassword']

    from datetime import datetime
    date=datetime.now().strftime("%Y%m%d-%H%M%S")
    import base64
    a=base64.b64decode(idproof)
    fh=open("E:\\bus\\web\\SmartBusLocator\\media\\user\\" +date+".jpg","wb")
    path="/media/user/"+date+'.jpg'
    fh.write(a)
    fh.close()


    lobj=Login()
    lobj.username=email
    lobj.password=password
    lobj.type='user'
    lobj.save()

    if password == conformpassword:
        obj=User()
        obj.name=name
        obj.phoneno=phoneno
        obj.email=email
        obj.place=place
        obj.post=post
        obj.pincode=pincode
        obj.district=district
        obj.idproof=path
        obj.LOOGIN=lobj
        obj.save()
    return JsonResponse({'status':'ok'})

def edit(request):
    name=request.POST['name']
    phoneno = request.POST['phoneno']
    email = request.POST['email']
    place = request.POST['place']
    post = request.POST['post']
    pincode =request.POST['pincode']
    district =request.POST['district']
    idproof=request.POST['idproof']
    lid=request.POST['lid']

    from datetime import datetime
    date=datetime.now().strftime("%Y%m%d-%H%M%S")
    import base64
    a=base64.b64decode(idproof)
    fh=open("C:\\Users\\DELL\\PycharmProjects\\SmartBusLocator\\media\\" +date+".jpg","wb")
    path="/media/"+date+'.jpg'
    fh.write(a)
    fh.close()
    obj=User.objects.get(LOOGIN_id=lid)

    if len(idproof)>0:
        obj.idproof = path
        obj.save()

    lobj=Login.objects.get(id=lid)
    lobj.username=email

    lobj.save()

    obj.name=name
    obj.phoneno=phoneno
    obj.email=email
    obj.place=place
    obj.post=post
    obj.pincode=pincode
    obj.district=district
    obj.save()
    return JsonResponse({'status':'ok'})


def logins(request):
    username=request.POST['name']
    password=request.POST['password']
    log=Login.objects.filter(username=username,password=password)
    if log.exists():
        log1=Login.objects.get(username=username,password=password)
        lid=log1.id
        if log1.type == 'user':
            return JsonResponse({'status':'ok','lid': str(lid),'type':log1.type})
        elif log1.type == 'driver':
            return JsonResponse({'status':'ok','lid': str(lid),'type':log1.type})
        else:
            return JsonResponse({'status':'No'})
    else:
        return JsonResponse({'status': 'No'})


def viewbuslocation(request):
    baj=Location.objects.all()
    l=[]
    for i in baj:
        l.append({'id':i.id,'bus':i.BUS.busregno,'placename':i.placename,'longitude':i.longitude,'latitude':i.latitude})

    return JsonResponse({'status':'ok','data':l})

def viewbusdetails(request):
    se=request.POST['search']
    baj = Bus.objects.filter(busregno__icontains=se)
    l = []
    for i in baj:
        lc = Location.objects.filter(BUS_id=i.id)
        if lc.exists():
            j = lc[0]
            l.append({'id': i.id, 'rid': i.ROUTE.id, 'busregno': i.busregno, 'busmodel': i.busmodel,
                      'chasisnumber': i.chasisnumber, 'manufacturename': i.manufacturename,
                      'route': i.ROUTE.routename, "latitude": j.latitude, "longitude": j.longitude})
    if Busstop.objects.filter(placename__icontains=se).exists():
        baj = Busstop.objects.filter(placename__icontains=se)
        l = []
        for i in baj:
            lc = Location.objects.filter(BUS__ROUTE__busstop__placename__icontains=se)
            if lc.exists():
                j = lc[0]
                l.append({'id': i.id, 'rid': i.ROUTE.id, 'busregno': j.BUS.busregno, 'busmodel': j.BUS.busmodel,
                          'chasisnumber': j.BUS.chasisnumber, 'manufacturename': j.BUS.manufacturename,
                          'route': i.ROUTE.routename, "latitude": j.latitude, "longitude": j.longitude})

    return JsonResponse({'status':'ok','data':l})



def viewbusdetails2(request):
    # Get the 'from' and 'to' bus stop names from the POST request
    from_place = request.POST['from']
    to_place = request.POST['to']
    print(from_place)
    print(to_place)


    # Get the bus stops with the specified names
    from_bus_stop = Busstop.objects.filter(placename__icontains=from_place).first()
    print(from_bus_stop,'fff')
    to_bus_stop = Busstop.objects.filter(placename__icontains=to_place).first()
    print(to_bus_stop,'tttt')

    if from_bus_stop is None or to_bus_stop is None:
        routes_from = Route.objects.filter(fromplace__icontains=from_place)
        print(routes_from, 'hhh', from_bus_stop)
        routes_to = Route.objects.filter(toplace__icontains=to_place)
        print(routes_to, 'www', from_bus_stop)

        # Get the common routes passing through both 'from' and 'to' bus stops
        common_routes = routes_from.filter(id__in=routes_to)

        bus_details = []
        print("dzcx", bus_details)
        for route in common_routes:
            # Get buses associated with the common route
            buses = Bus.objects.filter(ROUTE=route)

            # Iterate over each bus
            for bus in buses:
                # Get the location of the bus
                location = Location.objects.filter(BUS=bus).first()

                # Construct bus details dictionary
                bus_info = {
                    'id': bus.id,
                    'rid': route.id,
                    'busregno': bus.busregno,
                    'busmodel': bus.busmodel,
                    'chasisnumber': bus.chasisnumber,
                    'manufacturename': bus.manufacturename,
                    'route': route.routename,
                    'latitude': location.latitude if location else None,
                    'longitude': location.longitude if location else None
                }
                bus_details.append(bus_info)

        return JsonResponse({'status': 'ok', 'data': bus_details})
        # return JsonResponse({'status': 'error', 'message': 'Invalid bus stop names'})

    # Get the routes passing through the 'from' and 'to' bus stops
    routes_from = Route.objects.filter(busstop_id=from_bus_stop.id)
    print(routes_from,'hhh',from_bus_stop.id)
    routes_to = Route.objects.filter(busstop_id=to_bus_stop.id)
    print(routes_to,'www',from_bus_stop.id)

    # Get the common routes passing through both 'from' and 'to' bus stops
    common_routes = routes_from.filter(id__in=routes_to)

    bus_details = []
    print("dzcx",bus_details)
    for route in common_routes:
        # Get buses associated with the common route
        buses = Bus.objects.filter(ROUTE=route)

        # Iterate over each bus
        for bus in buses:
            # Get the location of the bus
            location = Location.objects.filter(BUS=bus).first()

            # Construct bus details dictionary
            bus_info = {
                'id': bus.id,
                'rid': route.id,
                'busregno': bus.busregno,
                'busmodel': bus.busmodel,
                'chasisnumber': bus.chasisnumber,
                'manufacturename': bus.manufacturename,
                'route': route.routename,
                'latitude': location.latitude if location else None,
                'longitude': location.longitude if location else None
            }
            bus_details.append(bus_info)

    return JsonResponse({'status': 'ok', 'data': bus_details})


def _update_location(request):
    lid=request.POST['lid']
    lat=request.POST['lat']
    lon=request.POST['lon']
    dobj=Location()
    if Location.objects.filter(BUS_id=lid).exists():
        dobj = Location.objects.get(BUS_id=lid)
    dobj.latitude=lat
    dobj.longitude=lon
    dobj.BUS_id=lid
    dobj.save()
    return JsonResponse({'status':'ok'})



def add_sched(request):
    time=request.POST['time']
    bid=request.POST['bid']
    trip=request.POST['trip']
    bustop=request.POST['bustop']
    dobj=Schedule()
    dobj.BUS_id=bid
    dobj.trip=trip
    dobj.time=time
    dobj.BUSSTOP_id=bustop
    dobj.save()
    return JsonResponse({'status':'ok'})

def delesch(request):
    id=request.POST['id']
    Schedule.objects.get(id=id).delete()
    return JsonResponse({'status':'ok'})

def notifiesupcomingbus(request):
    rid=request.POST['rid']
    aj = Busstop.objects.filter(ROUTE_id=rid)
    l=[]
    for i in aj:
        l.append({'id':i.id,'placename':i.placename,'longitude':i.longitude,'latitude':i.latitude,'Route':i.ROUTE.routename})

    return JsonResponse({'status':'ok','data':l})
def driveviewallo(request):
    lid=request.POST['lid']
    aj = Allocate.objects.filter(DRIVER__LOGIN_id=lid)
    l=[]
    for i in aj:
        l.append({'id':i.id,'rid':i.BUS.id,'busregno':i.BUS.busregno,'chasisnumber':i.BUS.chasisnumber,'manufacturename':i.BUS.manufacturename,'Route':i.BUS.ROUTE.routename})

    return JsonResponse({'status':'ok','data':l})
def drivesched(request):
    bid=request.POST['bid']
    aj = Schedule.objects.filter(BUS_id=bid)
    l=[]
    for i in aj:
        l.append({'id':i.id,'time':i.time,'trip':i.trip,'placename':i.BUSSTOP.placename})

    return JsonResponse({'status':'ok','data':l})

def recieveemergencynotification(request):
    bj = EmergencyNotification.objects.all()
    l=[]
    for i in bj:
        l.append({'id':i.id,'notification':i.notification,'date':i.date})
    return JsonResponse({'status':'ok','data':l})


def user_Changepassword(request):
    lid=request.POST["lid"]
    cpassword=request.POST["currentpassword"]
    npassword=request.POST["newpassword"]
    if Login.objects.filter(id=lid,password=cpassword).exists():

     obj=Login.objects.get(id=lid)
     obj.password=npassword
     obj.save()
     return JsonResponse({'status':'ok'})
    else:
        return JsonResponse({'status':'no'})

def user_vprofile(request):
    lid=request.POST['lid']
    i=User.objects.get(LOOGIN_id=lid)
    return JsonResponse({'status':'ok','name':i.name,'phoneno':i.phoneno,'email':i.email,'place':i.place,
                         'post':i.post,'pincode':i.pincode,'district':i.district,'idproof':i.idproof})
def drive_vprofile(request):
    lid=request.POST['lid']
    i=Driver.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok','name':i.name,'phoneno':i.phone,'email':i.email,'idproof':i.image})


def View_election_for_nomination(request):
    rid=request.POST['rid']
    sf = Busstop.objects.filter(ROUTE_id=rid)
    l = []
    for i in sf:
        l.append({'id': i.id, 'election_name': i.placename})

    # print(l)
    return JsonResponse({'status': 'ok', 'data': l})
from math import radians, sin, cos, sqrt, atan2

def distloc(request):
    userlat = request.POST['userlat']
    userlong = request.POST['userlong']
    buslat = request.POST['buslat']
    buslong = request.POST['buslong']
    bid = request.POST['bid']

    lat1 = radians(float(userlat))
    lon1 = radians(float(buslong))
    lat2 = radians(float(buslat))
    lon2 = radians(float(userlong))

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of Earth in kilometers
    distance_km = "{:.2f}".format(distance)
    time_hours = distance / 30
    esttime="{:.1f}".format(time_hours)


    print(distance_km,"km")
    print(esttime,"Total time")

    baj = Bus.objects.filter(id=bid)
    l = []
    for i in baj:
        l.append({'id': i.id, 'busregno': i.busregno, 'busmodel': i.busmodel,
                  'chasisnumber': i.chasisnumber, 'manufacturename': i.manufacturename,
                  'route': i.ROUTE.routename, "latitude": "no", "longitude": "no","distance_km":distance_km,"esttime":esttime})
    return JsonResponse({'status':'ok',"data":l})

def distlocstop(request):
    userlat = request.POST['userlat']
    userlong = request.POST['userlong']
    buslat = request.POST['buslat']
    buslong = request.POST['buslong']

    lat1 = radians(float(userlat))
    lon1 = radians(float(buslong))
    lat2 = radians(float(buslat))
    lon2 = radians(float(userlong))

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of Earth in kilometers
    distance_km = "{:.2f}".format(distance)
    time_hours = distance / 30
    esttime="{:.1f}".format(time_hours)


    print(distance_km,"km")
    print(esttime,"Total time")

    return JsonResponse({'status':'ok',"dist":distance_km,"tim":esttime})

