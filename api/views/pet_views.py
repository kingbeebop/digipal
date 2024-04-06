from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Pet
from ..serializers import PetSerializer

@api_view(['GET', 'POST'])
def pets_list(request):
    if request.method == 'GET':
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PetSerializer(pet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def my_pet(request):
    if request.user:
        user = request.user
        pet = Pet.objects.get(user=user)
        serializer = PetSerializer(pet)
        if serializer.is_valid():
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)