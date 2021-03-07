from django.urls import path
from . import views

urlpatterns = [

    path('',views.loginusr,name="loginpage"),
    path('home/',views.home,name='homepage'),
    path('about/',views.about,name='aboutpage'),
    path('contact/',views.contact,name='contactpage'),
    path('gallery/',views.gallery,name='gallerypage'),
    path('careers/',views.careers,name='careerpage'),
    path('studentadd/',views.student,name='studenformpage'),
    path('teacheradd',views.teacher,name='teacherformpage'),
    path('register/',views.createuser,name='registerpage'),
    path('logout/',views.logoutusr,name='logoutpage'),
    path('email/',views.emailsend,name='emailpage'),
    path('viewstd',views.viewstudents,name='viewstdpage'),
    path('leaveapplication',views.leaveform,name='leaveapplicationpage')

]