from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import SongSerializer
from .models import Song
from albums.models import Album
import ipdb

class SongView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.request.parser_context['kwargs']['pk'])
        ipdb.set_trace()
        
        return serializer.save(album=album)

    # def get(self, request, pk):
    #     """
    #     Obtençao de musicas
    #     """
    #     songs = Song.objects.filter(album_id=pk)

    #     result_page = self.paginate_queryset(songs, request)
    #     serializer = SongSerializer(result_page, many=True)

    #     return self.get_paginated_response(serializer.data)

    # def post(self, request, pk):
    #     """
    #     Criaçao de musica
    #     """
    #     album = get_object_or_404(Album, pk=pk)

    #     serializer = SongSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(album=album)

    #     return Response(serializer.data, status.HTTP_201_CREATED)
