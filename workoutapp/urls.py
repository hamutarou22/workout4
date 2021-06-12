from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('newevent/', views.neweventfunc, name='newevent'),
    path('newevent2/', views.neweventfunc2, name='newevent2'),
    path('record/', views.recordfunc, name='record'),
    path('change/', views.changefunc, name='change'),
    path('table/', views.tablefunc, name='table'),
    path('signup/', views.signupfunc, name='signup'),
    path('login/', views.loginfunc, name='login'),
    path('logout/', views.logoutfunc, name='logout'),
]