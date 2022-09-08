from django.shortcuts import render
# # from rest_framework.generics import (ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView)
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
# # from rest_framework.views import APIView
# # from rest_framework.generics import CreateView, UpdateView, DeleteView


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
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'home.html',{'movies':movies})

    def post(self,request,format=None):
        excel_file = request.FILES['movie_data']
        excel_file = request.FILES["movie_data"]
        filename = fs.save(excel_file.name,excel_file) 
        file_url = settings.PROJECT_APPS + fs.url(filename) # project app url + filename
        file_name=filename.split(".")[-1]
        if file_name == 'ods':
        # wb = xlrd.open_workbook(file_url)
            import pandas as pd
            df=pd.read_excel(file_url, engine='odf')
            print(df)

            for index, row in df.iterrows():
                name = row['name']
                actors = row['actors']
                release_date = row['release_date']
                poster_image = row['poster_image']
                geners = row['genres']
                move = Movie.objects.update_or_create(
                name=name,
                actor=actors,
                release_date=release_date,
                poster_image=poster_image,
                genres=geners,    
            )
        elif file_name == 'xlsx':
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
        else:
            print("Please provide .ods or .xlsx file")
            return Response('Please provide .ods or .xlsx file',status=status.HTTP_404_NOT_FOUND)
        return Response('File Uploaded Succesfully',status=status.HTTP_201_CREATED)

    

from django.contrib import messages
from django.shortcuts import redirect,render
from .forms import MovieForm
from .models import Movie
import pandas as pd
from django.db.models import Q

# Create your views here.

def home(request):
    form = MovieForm()

    if request.method == "POST":
        
        file = request.FILES.get('myfile')
        # excel_file = request.FILES["movie_data"]
        filename = fs.save(file.name,file) 
        file_url = settings.PROJECT_APPS + fs.url(filename) # project app url + filename
        file_name=filename.split(".")[-1]
        if file_name == 'xlsx':
            import pandas as pd
            df = pd.read_excel(file)
            print(df)
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
        elif file_name == 'ods':
        # wb = xlrd.open_workbook(file_url)
            import pandas as pd
            df=pd.read_excel(file_url, engine='odf')
            print(df)

            for index, row in df.iterrows():
                name = row['name']
                actors = row['actors']
                release_date = row['release_date']
                poster_image = row['poster_image']
                geners = row['genres']
                move = Movie.objects.update_or_create(
                name=name,
                actor=actors,
                release_date=release_date,
                poster_image=poster_image,
                genres=geners,    
            )
        else:
            print("Please provide .ods or .xlsx file")
            # return Response('Please provide .ods or .xlsx file',status=status.HTTP_404_NOT_FOUND)
        
        
        messages.success(request, 'Upload file succesfuly')
        movies =Movie.objects.all()
        return render(request, 'index.html',{'movies':movies})

    else:    
        filter_params = None
        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params= Q(name__icontains=key.strip()) | Q(actor__icontains=key.strip()) | Q(genres__icontains=key.strip())
                        # multiple_q = Q(Q(name__icontains=q) | Q(actor__icontains=q))
                        # filter_params = Q(name__icontains=key.strip())| Q(actor__icontains=key.strip())
                        # filter_params = Q(name__icontains=key.strip())
                        # filter_params = Q(actor__icontains=key.strip())
                        # filter_params = Q(genres__icontains=key.strip())


                    else:
                        filter_params |= Q(name__icontains=key.strip())
                        filter_params |= Q(actor__icontains=key.strip())


        movies = Movie.objects.filter(filter_params) if filter_params else Movie.objects.all()
    return render(request, 'index.html',{'movies':movies})