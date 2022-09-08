from django.contrib import admin
from django.urls import path
# from django.urls import include
from movie_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
#     # path('api/v1/movie_app',include("movie_app.urls"))
    path('movieapi/', views.MovieListView.as_view ()),
#     # path('createapi/', views.MovieCreateView.as_view ()),
#     # path('updateapi/<int:pk>/', views.MovieUpdateApi.as_view ()),
    path('<int:pk>/deleteapi/', views.MovieDeleteApi.as_view ()),


    path('excelapi/', views.SendExelView.as_view ()),
    path('', views.home ,name='movie_data'),
    
#     # path('upload/', views.MovieView.as_view ())
# ]
    # path('movie/', include('movie_app.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('movie_app.urls')),
# ]