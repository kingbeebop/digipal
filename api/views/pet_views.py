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
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Directly use request.data but modify state, hunger, and energy before saving
            # Prepare new pet data with default values for some fields
            new_pet_data = request.data.copy()  # Create a mutable copy of request.data
            new_pet_data['state'] = "idle"
            new_pet_data['hunger'] = 50
            new_pet_data['energy'] = 50

            # Initialize the serializer with the new data
            serializer = PetSerializer(data=new_pet_data)

            if serializer.is_valid():
                # Save the new pet instance with the current user assigned to it
                pet_instance = serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            # Return errors if the data is not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Return a 403 Forbidden response if the user is not authenticated
        return Response(status=status.HTTP_403_FORBIDDEN)


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
    if request.user.is_authenticated:
        try:
            # Assuming a user can have multiple pets, you might want to change this to filter().
            # For this example, I'll keep it as get() for simplicity.
            pet = Pet.objects.get(user=request.user)
            serializer = PetSerializer(pet)
            return Response(serializer.data)  # Return the serialized pet data
        except Pet.DoesNotExist:
            # If the pet does not exist, return an appropriate message
            return Response({"message": "Pet not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        # If the user is not authenticated, return a 403 Forbidden response
        return Response({"message": "Authentication required"}, status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def feed_pet(request):
    try:
        user = request.user
        pet = Pet.objects.get(user=user)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    new_hunger = pet.hunger + 10
    pet.hunger = new_hunger
    pet.save()

    serializer = PetSerializer(pet)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def play_pet(request):
    try:
        user = request.user
        pet = Pet.objects.get(user=user)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    new_energy = pet.energy - 10
    pet.energy = new_energy
    pet.save()

    serializer = PetSerializer(pet)
    return Response(serializer.data, status=status.HTTP_200_OK)