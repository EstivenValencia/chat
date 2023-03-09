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

class RetrieveRoom(APIView):
    def get(self, request):
        room = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(room, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Room(APIView):
	def get(self, request, user_id_from, user_id_to):
		room = list(ChatRoom.objects.filter(name=user_id_from+"_"+user_id_to))
		if len(room) <= 0:
			room = list(ChatRoom.objects.filter(name=user_id_to+"_"+user_id_from))
			if len(room) <= 0:
				room = ChatRoom(name=user_id_from+"_"+user_id_to)
				room.save()
		chats = Chat.objects.filter(room=room)
		serializer = ChatSerializer(chats, many=True)
		dict = {"room_name":room.name, "chats":serializer.data}
		return Response(dict, status=status.HTTP_200_OK)
