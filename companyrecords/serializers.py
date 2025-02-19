from rest_framework import serializers
from .models import Company, SwitchIP, FollowUp

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class SwitchIPSerializer(serializers.ModelSerializer):

    class Meta:
        model = SwitchIP
        fields = "__all__"
        read_only_fields = ['company']

class FollowUPSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = "__all__"
        read_only_fields = ['company']


