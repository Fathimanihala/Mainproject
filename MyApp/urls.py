"""
URL configuration for SmartBusLocator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login),
    path('changepass/',views.changepass),
    path('busadds/',views.busadds),
    path('busview/',views.busviews),
    path('allocateviews/',views.allocateviews),
    path('driveviews/',views.driveviews),
    path('busdelete/<id>',views.busdelete),
    path('allodelete/<id>',views.allodelete),
    path('drivedelete/<id>',views.drivedelete),
    path('busedits/<id>',views.busedits),
    path('driveedit/<id>',views.driveedit),
    path('driveedit_post/',views.driveedit_post),
    path('busedits_post/',views.busedits_post),
    path('busstopadds/',views.busstopadds),
    path('driveallocate/',views.driveallocate),
    path('driveallocate_post/',views.driveallocate_post),
    path('busstopviews/',views.busstopviews),
    path('busstopdelete/<id>',views.busstopdelete),
    path('busstopedits/<id>',views.busstopedits),
    path('busstopedits_post/',views.busstopedits_post),
    path('routeadds/', views.routeadds),
    path('routeedits/<id>', views.routeedits),
    path('routeviews/', views.routeviews),
    path('routedelete/<id>',views.routedelete),
    path('locations/',views.locations),
    path('notification/', views.notification),
    path('notification_post/', views.notification_post),
    path('adminnviewnotification/',views.adminnviewnotification),
    path('notificationdelete/<id>',views.notificationdelete),
    path('emergencynotify/',views.emergencynotify),
    path('emergencynotify_post/',views.emergencynotify_post),
    path('adminnewemergencynotification/',views.adminnewemergencynotification),
    path('emergencynotificationdelete/<id>',views.emergencynotificationdelete),
    path('user/',views.user),
    path('searchuser/',views.searchuser),
    path('adminhomepage/',views.adminhomepage),
    path('login_post/',views.login_post),
    path('changepass_post/', views.changepass_post),
    path('routeadds_post/', views.routeadds_post),
    path('routeedits_post/', views.routeedits_post),
    path('routeadds_post/', views.routeadds_post),
    path('busadds_post/',views.busadds_post),
    path('busstopadds_post/',views.busstopadds_post),
    path('user_Changepassword/',views.user_Changepassword),
    path('driveadds/',views.driveadds),
    path('driveadds_post/',views.driveadds_post),





    path('registration/',views.registration),
    path('edit/',views.edit),
    path('logins/',views.logins),
    path('viewbuslocation/',views.viewbuslocation),
    path('viewbusdetails/',views.viewbusdetails),
    path('viewbusdetails2/',views.viewbusdetails2),
    path('notifiesupcomingbus/',views.notifiesupcomingbus),
    path('driveviewallo/',views.driveviewallo),
    path('drivesched/',views.drivesched),
    path('_update_location/',views._update_location),
    path('add_sched/',views.add_sched),
    path('delesch/',views.delesch),
    path('distloc/',views.distloc),
    path('distlocstop/',views.distlocstop),

    path('recieveemergencynotification/',views.recieveemergencynotification),
    path('user_vprofile/',views.user_vprofile),
    path('drive_vprofile/',views.drive_vprofile),
    path('View_elenamein_nomination/',views.View_election_for_nomination),
]