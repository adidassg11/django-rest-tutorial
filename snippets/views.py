from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    # if request.method == 'GET':
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        # return JsonResponse(serializer.data, safe=False)  # Old django style
        return Response(serializer.data)

    #elif request.method == 'POST':
    def post(self, request, format=None):
        # data = JSONParser().parse(request)  # Old Django style
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)  # Old django style
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(serializer.errors, status=400)  # Old Django style
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
class SnippetDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            # return Response(status=status.HTTP_404_NOT_FOUND)
            raise Http404

    #if request.method == 'GET':
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(data=serializer.data)

    #elif request.method == 'PUT':
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #elif request.method == 'DELETE':
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)