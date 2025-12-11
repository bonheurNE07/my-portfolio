from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]
