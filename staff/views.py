from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# Create your views here.
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect

from django.http import HttpResponse
from django.views import generic
from .models import staffInfo
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import RegistrationForm, UserLoginForm, UserChangePasswordForm, UserEditProfileForm
from django.contrib.auth.models import User


# importing modules
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Permission

def add_user_to_group_perm(username):
        content_type = ContentType.objects.get_for_model(staffInfo)     
        stafft_permission = Permission.objects.filter(content_type=content_type)
        for perm in stafft_permission:
            print(perm.codename, username)
            if (perm.codename == 'add_staffinfo' or perm.codename == 'delete_staffinfo' or perm.codename == 'view_staffinfo') and username == 'editor' :
                user = User.objects.get(username=username)
                permission = Permission.objects.get(codename=perm.codename)
                user.user_permissions.add(permission)
                get_user_model().objects.get(username = username)
            if (perm.codename == 'change_staffinfo' or perm.codename == 'view_staffinfo') and username == 'viewer':
                print('match this condition ::::::::::::::::::::::::::::::::::::')
                user = User.objects.get(username=username)
                permission = Permission.objects.get(codename=perm.codename)
                user.user_permissions.add(permission)
                get_user_model().objects.get(username = username)
            else:
                continue
                
                # viewer_group.permissions.add(perm)
                # creator_group.permissions.add(perm)
                # viewer_group.save()
                # creator_group.save()
        # if username == 'creator':
        #     user = User.objects.get(username=username)
        #     user.groups.add(creator_group)
        #     user.save()
        #     print(':::::::::::::::::: user ::::::::::::::',user.has_perm('staff.add_staffinfo'))
        # elif username == 'viewer':
        #     user = User.objects.get(username=username)
        #     user.groups.add(viewer_group)
        #     user.save()
        # else:
        #     user = User.objects.get(username=username)
        #     user.groups.add(viewer_group)
        #     user.groups.add(creator_group)
        #     user.save()
            
            
class HomepageView(generic.TemplateView):
    template_name = 'home.html'
#change their password and redirect to profile
class ChangePasswordView(PasswordChangeView,SuccessMessageMixin ):
    form_class = UserChangePasswordForm
    success_url = '/account/profile'
    success_message = "Successfully Changed Your Password"
    template_name = 'accounts/changePassword.html'

def edit_profile(request,id):
    instance = User.objects.get(id=id)
    form = UserEditProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('staff:profile')
    return render(request, 'accounts/editProfile.html', {'form': form}) 

#sign up user with name and password
class SignUp(generic.FormView):
    template_name = 'accounts/signUp.html'
    form_class = RegistrationForm
    success_url='signIn'   
    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        try:
            username = form.cleaned_data['username']
            form.save()
        except:
            print('::::error::::::')
            messages.error(self.request, "Something went wrong, please try again !.")
        return valid
    
#login new user after they sign up 
class SignIn(generic.FormView):
    template_name = 'accounts/signIn.html'
    form_class = UserLoginForm    
    success_url = settings.LOGIN_REDIRECT_URL
    def form_valid(self, form):
        try:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(self.request, username=username, password=password)
            add_user_to_group_perm(username)
            user = User.objects.get(username=username)
            print(':::::::::::::::::: user perm ::::::::::::::',
                  user.has_perm('staff.add_staffinfo'),
                  user.has_perm('staff.change_staffinfo'),
                  user.has_perm('staff.view_staffinfo'),
                  user.has_perm('staff.delete_staffinfo'))
            login(self.request, user)
        except:
            messages.error(self.request, "Something went wrong, please try again !.")
        return super().form_valid(form)

#view user after sign up successfully
class ProfileView(generic.TemplateView):
    template_name = 'accounts/profile.html'

#log out and redirect to homepage directly
def logout_view(request):
    logout(request)
    return redirect('/')

class SignOutView(generic.TemplateView):
        def get(self, request: HttpRequest):
            try:
                logout(request)
                return redirect('/')
            except:
                messages.error(self.request, 'Something went wrong , please try again!..')
                
#view five staffs
class StaffView(LoginRequiredMixin,generic.ListView):
    login_url = settings.LOGIN_URL
    redirect_field_name = settings.LOGIN_REDIRECT_URL
    model = staffInfo
    context_object_name = 'staff_list'
    template_name = 'staff/index.html'
    ordering = 'id'
    paginate_by = 5
    def http_method_not_allowed(self, request: HttpRequest, *args, **kwargs):
        return super().http_method_not_allowed(request, *args, **kwargs)
    
    def get_queryset(self):
        print('call query:::::::::::', User.objects.get(username='creator').has_perm('staff:can_create_staff'))
        return staffInfo.objects.order_by('-id')
        

class DetailView(generic.DetailView):
    model = staffInfo
    context_object_name = 'staff_info'
    template_name = "staff/detail.html"
    # messages.success(request, message='Staff created!.')

class CreateStaff(PermissionRequiredMixin,SuccessMessageMixin,generic.CreateView):
     # specify the model for create view
    model = staffInfo
    template_name = 'staff/create_staff.html'
    permission_required = ('staff.add_staffinfo')
    # specify the fields to be displayed
    fields = ['name', 'sex', 'age']
    success_url = reverse_lazy('staff:index')
    
    def handle_no_permission(self) -> HttpResponse:
        print(self.request.path)
        return HttpResponse(content='<h1>No Permission, You can not do this action !</h1>')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, message='Staff created!.')
        return super(CreateStaff,self).form_valid(form)
        
    # def get_success_message(self, cleaned_data):
    #     return self.success_message % dict(
    #         cleaned_data,
    #         username=self.object.name,
    #     )

class UpdateStaff(PermissionRequiredMixin,generic.UpdateView): 
    # specify the model you want to use 
    login_url = "staff:prfile"
    model = staffInfo
    permission_required = ('staff.change_staffinfo')
    raise_exception = True
    permission_denied_message = "Permission Denied"
    template_name = 'staff/update_staff.html'
    # specify the fields 
    fields = [
        "name", 
        "sex"
    ] 
    success_url = reverse_lazy('staff:index')
    def handle_no_permission(self) -> HttpResponse:
        print(self.request.path)
        return HttpResponse(content='<h1>No Permission, You can not do this action !</h1>')
    
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, message='Staff updated!.')
        return HttpResponseRedirect(success_url)
  
    
class DeleteStaff(PermissionRequiredMixin,generic.DeleteView):
    model = staffInfo
    permission_required = ('staff.delete_staffinfo')
    template_name = 'staff/delete_staff.html'
    context_object_name = 'staff_deleted'
    success_url = reverse_lazy('staff:index')
    
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, message='Staff deleted!.')
        return HttpResponseRedirect(success_url)
    
    def handle_no_permission(self) -> HttpResponse:
        print(self.request.path)
        return HttpResponse(content='<h1>No Permission, You can not do this action !</h1>')



# class MyForm(forms.ModelForm):
# #     class Meta:
# #         model = staffInfo
# #         fields = ['name', 'sex', 'age']

# # def update_staff(request,id):
# #     instance = staffInfo.objects.get(id=id)
# #     form = MyForm(request.POST or None, instance=instance)
# #     if form.is_valid():
# #         form.save()
# #         return redirect('staff:index')
# #     # else:
# #     #     raise ValidationError(message="Error update!!")
#     return render(request, 'staff/update_staff.html', {'form': form}) 

