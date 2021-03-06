from django.urls import path, include
from .views import user_signup, user_login, user_logout, user_profile


urlpatterns = [

        path('signup/', user_signup, name='user-signup'),
        path('login/', user_login, name='user-login'),
        path('logout/', user_logout, name='user-logout'),
        path('profile/<int:pk>/', user_profile, name ='user-profile'),

]
