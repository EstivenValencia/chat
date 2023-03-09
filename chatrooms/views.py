from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Chat, ChatRoom
from .serializers import *

class Index(View):
	def get(self, request):
		return render(request, 'chatrooms/index.html')

class Room(APIView):
	def get(self, request, room_name):
		room = ChatRoom.objects.filter(name=room_name).first()
		chats = Chat.objects.filter(room=room)
		serializer = ChatSerializer(chats, many=True)
		if room is False:
			room = ChatRoom(name=room_name)
			room.save()
		dict = {"room_name":room_name, "chats":serializer.data}
		return Response(dict, status=status.HTTP_200_OK)
