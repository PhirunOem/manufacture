from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def viewStaff(request):
    return Response ({'message': 'this is staff'})
@api_view(['POST'])
def postStaff(request):
    return Response({'message':'Staff created !'})
@api_view(['PUT'])
def updateStaff(request):
    return Response({'message':'Staff updated !'})
@api_view(['DELETE'])
def deleteStaff(request):
        return Response({'message':'Staff deleted !'})

    
    