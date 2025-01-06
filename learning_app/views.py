from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import UserLogin,ContentUpload
from .Serializer import UserLoginSerializer,ContentUploadSerializer

class UserLoginViewSet(viewsets.ModelViewSet):
    queryset = UserLogin.objects.all()
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        """
        Overridden create method to ensure that no two users have the same email and role combination.
        """
        email = request.data.get('email')
        role = request.data.get('role')


        # Check if the combination of email and role already exists
        if UserLogin.objects.filter(email=email, role=role).exists():
            return Response({
                'error': 'A user with this email and role already exists.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # If combination is unique, proceed to create the user
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['post'])
    def login(self,request):
        email = request.data.get('email')
        name=request.data.get('name')
        role=request.data.get('role')
        if not email or not name or not role:
            return Response({'error': 'Email,name and role are required.'}, status=status.HTTP_400_BAD_REQUEST)


        try:
            user = UserLogin.objects.get(email=email,name=name,role=role)
            serializer = UserLoginSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserLogin.DoesNotExist:
            return Response({'error': 'Invalid email, name  or role combination.'}, status=status.HTTP_401_UNAUTHORIZED)


class ContentUploadViewSet(viewsets.ModelViewSet):
    queryset = ContentUpload.objects.filter(is_deleted=False)  # Exclude deleted content
    serializer_class = ContentUploadSerializer

