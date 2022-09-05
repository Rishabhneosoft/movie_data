from django.shortcuts import render
# from rest_framework.generics import (ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework.generics import ListAPIView,DestroyAPIView,UpdateAPIView
# from rest_framework.generics import ListAPIView

import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
import datetime 
import xlrd
from django.conf import settings
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage()
# from rest_framework.views import APIView
# from rest_framework.generics import CreateView, UpdateView, DeleteView


'''FILTER API IN DATABASE'''
class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','actor','release_date','genres']

class MovieUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDeleteApi(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SendExelView(APIView):
    def post(self,request,format=None):
        excel_file = request.FILES['movie_data']
        excel_file = request.FILES["movie_data"]
        filename = fs.save(excel_file.name,excel_file) 
        file_url = settings.PROJECT_APPS + fs.url(filename) # project app url + filename
        wb = xlrd.open_workbook(file_url)
        sheet = wb.sheet_by_index(0) 
        for i in range(sheet.nrows-1):
            if i == sheet.nrows-1: # row-1 
                break
            name = sheet.cell_value(i+1,0)
            actor = sheet.cell_value(i+1,1)
            # import datetime 
            release_date = sheet.cell_value(i+1,2)
            rls_date = datetime.datetime(*xlrd.xldate_as_tuple(release_date, wb.datemode))
            rls_date = rls_date.date()
            poster_image = sheet.cell_value(i+1,3)
            genres = sheet.cell_value(i+1,4)
            date = sheet.cell_value(0,2).split('/')
            move = Movie.objects.update_or_create(
                name=name,
                actor=actor,
                release_date=rls_date,
                poster_image=poster_image,
                genres=genres,
                
            )
        return Response('File Uploaded Succesfully',status=status.HTTP_201_CREATED)

        