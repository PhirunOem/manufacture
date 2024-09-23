from django.urls import path

from . import views
app_name = 'staff'
urlpatterns = [
    ## home url
    path('', views.HomepageView.as_view(), name='home'),
    ## for user authentication urls
    path('account/signUp', views.SignUp.as_view(), name='sign-up'),
    path('account/signIn', views.SignIn.as_view(), name='sign-in'),
    path('account/profile', views.ProfileView.as_view(), name='profile'),
    path('account/signOut', views.logout_view, name='logout'),
    path('account/changePassword', views.ChangePasswordView.as_view(), name ='change-password'),
    path('account/<int:id>/editProfile', views.edit_profile, name ='edit-profile'),
    
    ## for staff crud urls 
    path("staff/", views.StaffView.as_view(), name="index"),
    path("staff/<int:pk>/detail", views.DetailView.as_view(), name='detail'),
    path('staff/create/', views.CreateStaff.as_view(), name= 'create-staff'),
    # path('staff/<int:pk>/update', views.update_staff, name = 'update-staff'),
    path('staff/<int:pk>/update', views.UpdateStaff.as_view(), name = 'update-staff'),
    path('staff/<pk>/delete', views.DeleteStaff.as_view(), name = 'delete-staff'),

]
