from movie_api.views import *
from django.urls import path

urlpatterns = [
    path('random/', get_random_movie),
    path('all/', get_all_movies),
    path('search/', get_filter_movie),
    path('mark_view/', mark_view),
    path('rate-movie/', rate_movie),
    path('create_user/', register_user),
    path('auth_user/', CustomAuthToken.as_view()),
    path('register/', template_register),
    path('login/', template_login),
    path('get-random/', template_get_random),
    path('get-all/', template_get_all),
    path('search-movie/', template_search),
]
