from api.models import *
from project.models import *
from django.contrib.auth.models import User

from rest_framework.serializers import (
	ModelSerializer,
	SerializerMethodField,
	ReadOnlyField
	)

# Create your views here.

class MessageSerializer(ModelSerializer):
	class Meta:
		model = Message
		fields = '__all__'