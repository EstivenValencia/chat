from django.urls import path
from .views import *

urlpatterns = [
	path('', Index.as_view()),
	path('retrieve-user/', RetrieveUser.as_view()),
	path('retrieve-chat-room/', RetrieveAllChatRoom.as_view()),
	path('<str:user_id>', RetrieveChatRoom.as_view()),
]