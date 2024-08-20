from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import signup_view, logout_view



urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),

]