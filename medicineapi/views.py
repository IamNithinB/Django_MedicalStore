from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.status import(
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_302_FOUND
)
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import SignupSerializer,MedicineSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from medicine.models import MedicineModel



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def simpleapi(request):
    return Response({'text':'Hello World'},status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error':'Please Provide both username and password'},status=HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username,password=password)

    if not user:
        return Response({'error':'Invalid Credentials'},HTTP_404_NOT_FOUND)
    token,_ = Token.objects.get_or_create(user=user)
    return Response({'token':token.key},status=HTTP_200_OK)



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):

    obj = SignupSerializer(data=request.data)
    if obj.is_valid():
        obj.save()
        return Response({'Message':'Successfully Signed up'},status= HTTP_200_OK)

    return Response(obj.errors,status=HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMedic(request):

    medicine = MedicineModel.objects.all()
    serializer = MedicineSerializer(medicine,many=True)
    return Response(serializer.data)



@csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def postMedic(request):
 
    serializer = MedicineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=HTTP_200_OK)
    return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def editMedic(request,id):
    medicine = MedicineModel.objects.get(pk=id)
    serializer = MedicineSerializer(medicine,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=HTTP_200_OK)
    return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete(request,id):
    medicine = MedicineModel.objects.get(pk=id)
    medicine.delete()
    return Response(status=HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(["GET"])
@permission_classes(([IsAuthenticated]))
def viewMedic(request,id):

    medicine = MedicineModel.objects.get(pk=id)
    serializer = MedicineSerializer(medicine)
    return Response(serializer.data)

@csrf_exempt
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response({'Message':'Logged Out Successfully'})


# Create your views here.


