from django.urls import path
from .views import *

urlpatterns = [
	path('', Index.as_view(), name='index'),
	path('users/', RetrieveUser.as_view()),
	path('<user_id_from>/<user_id_to>', Room.as_view(), name='room'),
]