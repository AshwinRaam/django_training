from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from doubts.models import Trainer, Doubts
from doubts.serializers import TrainerSerializer, DoubtsSerializer


class Trainers(APIView):
    def get(self, request):
        queryset = Trainer.objects.all()
        serializer = TrainerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TrainerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DoubtsView(APIView):
    def get(self, request):
        queryset = Doubts.objects.all()
        serializer = DoubtsSerializer(queryset, many=True)
        return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def trainer(request, id):
#     trainer = get_object_or_404(Trainer, pk=id)
#     if request.method == 'GET':
#         serializer = TrainerSerializer(trainer)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = TrainerSerializer(trainer, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         trainer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
