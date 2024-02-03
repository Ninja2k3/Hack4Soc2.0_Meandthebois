from django.shortcuts import render
from django.http import Http404
from rest_framework import generics

from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status, permissions

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import *
from .serializers import *
