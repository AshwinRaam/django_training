from xml.parsers.expat import model
from rest_framework import serializers

from doubts.models import Trainer


class DoubtsSerializer(serializers.Serializer):
    name = serializers.CharField()
    question = serializers.CharField()
    answer = serializers.CharField()
    question_from = serializers.StringRelatedField()
    answer_by = serializers.StringRelatedField()
    when_asked = serializers.DateTimeField()
    status = serializers.CharField()


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['name', 'age', 'gender', 'phonenumber']

    phonenumber = serializers.CharField(source='contact_no')
