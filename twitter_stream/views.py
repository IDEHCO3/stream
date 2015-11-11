from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from stream.settings import AUTH_USER_MODEL

from twitter_stream.Serializers import MonitorTwitterSerializer, AccountTwitterSerializer, GeoTwitterSerializer
from twitter_stream.models import MonitorTwitter, AccountTwitter, GeoTwitter


# Create your vie ws here
#

class AccountTwitterListFiltered(generics.ListCreateAPIView):

    queryset = AccountTwitter.objects.all()

    serializer_class = AccountTwitterSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):

        user_name = self.kwargs.get("user_name")

        user = None

        if user_name is not None:

            try:
                user = AUTH_USER_MODEL.objects.get(username=user_name)

            except AUTH_USER_MODEL.DoesNotExist:

                user = None

        if user is not None:
            return self.queryset.filter( user=user)

        return self.queryset

class AccountTwitterDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = AccountTwitter.objects.all()

    serializer_class = AccountTwitterSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self):

        user = self.request.user

        queryset = AccountTwitter.objects.filter(user_id=user)

        return queryset.all().first()


class MonitorTwitterList(generics.ListCreateAPIView):

    queryset = MonitorTwitter.objects.all()

    serializer_class = MonitorTwitterSerializer


class MonitorTwitterListFiltered(generics.ListCreateAPIView):

    queryset = MonitorTwitter.objects.all()

    serializer_class = MonitorTwitterSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):

        user_name = self.kwargs.get("user_name")

        user = None

        if user_name is not None:

            try:
                user = AUTH_USER_MODEL.objects.get(username=user_name)

            except AUTH_USER_MODEL.DoesNotExist:

                user = None

        if user is not None:
            return self.queryset.filter(user_id=user)

        return self.queryset

class MonitorTwitterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonitorTwitter.objects.all()
    serializer_class = MonitorTwitterSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #authentication_classes = (JSONWebTokenAuthentication, )


class GeoTwitterListFiltered(generics.ListAPIView):

    queryset = GeoTwitter.objects.all()

    serializer_class = GeoTwitterSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):

        monitorName = self.kwargs.get("monitor_name")


        if monitorName is not None:


            return self.queryset.filter(monitor_twitter__name=monitorName)

        return self.queryset