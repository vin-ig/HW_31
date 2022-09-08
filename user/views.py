from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from user.models import User, Location
from user.serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, UserDestroySerializer, \
	LocationSerializer


class UserListView(ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
	queryset = User.objects.all()
	serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserDestroySerializer


class LocationViewSet(ModelViewSet):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
