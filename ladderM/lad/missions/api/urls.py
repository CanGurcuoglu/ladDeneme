from django.urls import path
from missions.api import views as api_views

urlpatterns = [
    path('missions/', api_views.UserListCreateAPIView.as_view(), name='user-list'), #herkes çıkıyor
    path('users/<int:pk>', api_views.UserDetailAPIView.as_view(), name='user-info'), #userlar id lere gore cikiyor
    path('users/<int:user_pk>/missions', api_views.MissionCreateAPIView.as_view(), name='mission-yap'), #user_pk nolu kişiye gorev ekliyor
    path('missions/<int:pk>', api_views.MissionDetailAPIView.as_view(), name='missions'), #id li grev cikior
]