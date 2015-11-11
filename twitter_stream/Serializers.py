from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from twitter_stream.models import AccountTwitter, MonitorTwitter, GeoTwitter


class AccountTwitterSerializer(ModelSerializer):

    class Meta:
        model = AccountTwitter
        fields = ['user', 'consumer_key', 'consumer_secret', 'consumer_token', 'consumer_token_secret']


class MonitorTwitterSerializer(ModelSerializer):

    class Meta:
        model = MonitorTwitter
        fields = ['user', 'name', 'description', 'initial_date',  'final_date', 'interval', 'created_on']


class GeoTwitterSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = GeoTwitter
        fields = ['monitor_twitter', 'id_twitter', 'text_twitter',  'user_id', 'user_screen_name', 'user_name', 'user_avatar', 'created_on']

















