from django.contrib.auth import get_user_model

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from study.core.models import Personaje
from .serializers import UserSerializer, PersonajeSerializer


class PersonajeViewSet(ListModelMixin, GenericViewSet):
    serializer_class = PersonajeSerializer
    queryset = Personaje.objects.all()
