from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from django.contrib.auth.models import User
from .serializers import *

class Index(View):
	def get(self, request):
		return render(request, 'chatrooms/index.html')

class RetrieveUser(APIView):
    def get(self, request):
        room = User.objects.all()
        serializer = UserSerializer(room, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveAllChatRoom(APIView):
    def get(self, request):
        room = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(room, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveChatRoom(APIView):
	def get(self, request, user_id):
		user_id_from = user_id.split('_')[0]
		user_id_to = user_id.split('_')[1]
		concat1 = f"{user_id_from}_{user_id_to}"
		try:
			room = ChatRoom.objects.get(name=concat1)
		except:
			try:
				concat = f"{user_id_to}_{user_id_from}"
				room = ChatRoom.objects.get(name=concat)
			except:
				print("ENTRO")
				room = ChatRoom(name=concat1)
				room.save()
		print(room.name)
		chats = ChatMessage.objects.filter(room=room)
		serializer = ChatMessageSerializer(chats, many=True)
		dict = {"room_name":room.name, "chats":serializer.data}
		return Response(dict, status=status.HTTP_200_OK)
