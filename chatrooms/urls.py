from django.urls import path
from .views import *

urlpatterns = [
	path('', Index.as_view(), name='index'),
	path('rooms/', RetrieveRoom.as_view()),
	path('<str:room_name>/', Room.as_view(), name='room'),
]