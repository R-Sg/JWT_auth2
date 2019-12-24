from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


def test_view(request):
    return HttpResponse("this is myapp view")


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return Response(data, status=404)
