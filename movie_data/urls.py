"""movie_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from django.urls import include
from movie_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/movie_app',include("movie_app.urls"))
    path('movieapi/', views.MovieListView.as_view ()),
    # path('createapi/', views.MovieCreateView.as_view ()),
    path('updateapi/<int:pk>/', views.MovieUpdateApi.as_view ()),
    path('<int:pk>/deleteapi/', views.MovieDeleteApi.as_view ()),


    path('excelapi/', views.SendExelView.as_view ()),


]