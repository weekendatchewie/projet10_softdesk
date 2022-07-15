from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.models import Project
from api.serializers import ProjectSerializer


class ProjectViewset(ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
