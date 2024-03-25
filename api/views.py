from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .models import Patient


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'login': 'Success'
        })
    
@api_view(['POST'])
def patient_view(request):
    if request.method == 'POST':
        data = request.data
        name = data.get('Name')
        email = data.get('Email')
        phone = data.get('Phone')
        xray = request.FILES.get('Xray')
        result = data.get('result')
        
        patient = Patient.objects.create(
            Name=name,
            Email=email,
            Phone=phone,
            Xray=xray,
            result=result
        )
        if result == 'Fractured':
            description = data.get('description_fractured')
            patient.fractured_info.create(description_fractured=description)
        elif result == 'Not Fractured':
            description = data.get('description_not_fractured')
            patient.non_fractured_info.create(description_not_fractured=description)

        return Response({"message": "Patient created successfully"}, status=201)

@api_view(['GET'])
def patientdisplay_view(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        data = []
        for patient in patients:
            patient_data = {
                "Name": patient.Name,
                "Email": patient.Email,
                "Phone": patient.Phone,
                "Xray": patient.Xray.url if patient.Xray else None,
                "result": patient.result,
            }
            if patient.result == 'Fractured':
                patient_data["description_fractured"] = patient.fractured_info.description_fractured
            elif patient.result == 'Not Fractured':
                patient_data["description_not_fractured"] = patient.non_fractured_info.description_not_fractured
            data.append(patient_data)
        return Response(data)
