from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from doubts.models import Trainer, Doubts
from doubts.serializers import TrainerSerializer, DoubtsSerializer


class TrainersListCreate(ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class TrainerRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class DoubtsView(APIView):
    def get(self, request):
        queryset = Doubts.objects.all()
        serializer = DoubtsSerializer(queryset, many=True)
        return Response(serializer.data)
