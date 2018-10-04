from django.urls import path
#from django.contrib.auth  import views as auth_views
from . import views 

#app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.registrarse, name='login'),
    #path('log_in', auth_views.login, name ='login'),

]