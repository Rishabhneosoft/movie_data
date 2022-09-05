# from django.contrib import admin
# from django.urls import path
# # from django.urls import include


# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     # path('api/v1/movie_app',include("movie_app.urls"))
# ]


# from django.urls import path, include
# from .views import *
# # from dj_app.views import EmployeeViewSet
# # from rest_framework.routers import DefaultRouter


# # router = DefaultRouter()
# # router.register('', EmployeeViewSet, basename='employee')
# # urlpatterns = router.urls

# urlpatterns = [
#     # path('employee/',include(router.urls)),
#     # path('employee/create/', EmployeeCreate.as_view(), name='employee-create'),
#     # path('employee/update/', EmployeeUpdate.as_view(), name='employee-update'),
#     path('item/create/', ItemAPI.as_view(), name='item-create'),
#     path('employee/create/', EmployeeAPI.as_view(), name='employee-create'),
# ]