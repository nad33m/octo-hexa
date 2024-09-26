from rest_framework import serializers
from .models import *

class CsInfoSerializer(serializers.ModelSerializer):
	class Meta:
            model = CsInfo
            fields = "__all__"