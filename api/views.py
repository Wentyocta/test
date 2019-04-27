from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from api.models import *
from api.serializer import *
import json
from datetime import datetime
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# Create your views here.
class messageList(APIView):
	def get(self, request):
		messages = Message.objects.all()
		messageSerializer = MessageSerializer(messages, many=True)

		return Response({
			'messages' : messageSerializer.data,
		},
		status=HTTP_200_OK)

	def post(self, request, *args, **kwargs):
		message_text = request.data['message']

		try:
			message = Message()
			message.text = message_text
			message.success = True
			message.created_date = datetime.now()
		except Exception as e:
			raise e

		return Response(None, status=HTTP_200_OK) 

class getMessage(APIView):
	def get(self, request, *args, **kwargs):
		message_id = int(self.kwargs['message_id'])

		try:
			message = Message.objects.get(pk=message_id)
			messageSerializer = MessageSerializer(message)

			return Response({
				'messages' : messageSerializer.data,
			},
			status=HTTP_200_OK)
		except Message.DoesNotExist:
			return Response({'error': 'message does not exists'}, status=HTTP_400_BAD_REQUEST)