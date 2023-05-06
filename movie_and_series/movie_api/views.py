from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from movie_api.models import Movie, View, Rating
from movie_api.serializers import MovieSerializer, UserSerializer
from django.shortcuts import render
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def get_random_movie(request):
    movie = Movie.objects.order_by('?').first()
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_movies(request):
    sort_by = request.GET.get('sort_by', 'name')
    if sort_by == 'name':
        movies = Movie.objects.order_by('name')
    elif sort_by == 'genre':
        movies = Movie.objects.order_by('genre')
    elif sort_by == 'type':
        movies = Movie.objects.order_by('type')
    elif sort_by == 'rating':
        movies = Movie.objects.order_by('-average_rating')
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_filter_movie(request):
    name = request.GET.get('name')
    type = request.GET.get('type')
    genre = request.GET.get('genre')

    movies = Movie.objects.all()
    if name:
        movies = movies.filter(name__icontains=name)
    if type:
        movies = movies.filter(type=type)
    if genre:
        movies = movies.filter(genre__name=genre)

    serealizer = MovieSerializer(movies, many=True)
    return Response(serealizer.data)


@api_view(['POST'])
def mark_view(request):
    user = request.user
    movie_id = request.data.get('movie_id')
    movie = Movie.objects.get(id=movie_id)
    if movie:
        view, created = View.objects.get_or_create(user=user, movie=movie)
        view.view = True
        view.save()
    movie = Movie.objects.get(id=movie_id)
    return Response({'message': 'success', 'views': movie.views})


@api_view(['POST'])
def rate_movie(request):
    movie_id = request.data.get('movie_id')
    rating_value = request.data.get('rating')

    # Obtener la película y la calificación existente (si existe)
    movie = get_object_or_404(Movie, id=movie_id)
    rating, created = Rating.objects.get_or_create(
        movie=movie, user=request.user, rating=rating_value)

    # Si la calificación ya existe, actualizarla con la nueva calificación
    if not created:
        return Response({'message': 'Movie already rated.'})
    else:
        rating.num_ratings += 1

    # Actualizar la calificación total y guardar la calificación
    rating.total_rating += float(rating_value)
    rating.save()

    # Actualizar la calificación promedio de la película
    movie.average_rating = rating.total_rating / rating.num_ratings
    movie.save()

    return Response({'message': 'Movie rated successfully.', 'rating': movie.average_rating})


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        token, created = Token.objects.get_or_create(user=user)
        return Response({"data": serializer.data, "token": token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


def template_login(request):
    return render(request, 'login.html')


def template_register(request):
    return render(request, 'register.html')


def template_get_random(request):
    return render(request, 'random.html')


def template_get_all(request):
    return render(request, 'all.html')


def template_search(request):
    return render(request, 'search.html')
