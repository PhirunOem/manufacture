from django.urls import path
from . import views
app_name = 'staffAPI'
urlpatterns = [
    #CRUD
    path('v1/view',views.viewStaff,name='viewStaff'),
    path('v1/create',views.postStaff,name='postStaff'),
    path('v1/update',views.updateStaff,name='updateStaff'),
    path('v1/delete',views.deleteStaff,name='deleteStaff')
]
