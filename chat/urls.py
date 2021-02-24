from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register,name='register'),
    path('chat/',views.messages,name='messages'),
    path('send/<int:convo_id>',views.send_message,name='send_message'),
    path('updates/',views.get_updates,name='get_updates'),
    path('new/',views.new_msg,name='new_msg'),


]