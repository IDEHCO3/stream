from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from twitter_stream_api.models import AccountTwitter, MonitorTwitter, GeoTwitter


class AccountTwitterSerializer(ModelSerializer):

    class Meta:
        model = AccountTwitter
        fields = ['user', 'consumer_key', 'consumer_secret', 'consumer_token', 'consumer_token_secret']

class MonitorTwitterSerializer(ModelSerializer):

    class Meta:
        model = MonitorTwitter
        fields = ['user', 'name', 'description', 'search_term', 'initial_date',  'final_date', 'interval', 'since_id', 'created_on']

class GeoTwitterSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = GeoTwitter
        geo_field = 'geom'
        fields = ['monitor_twitter', 'twitter_id', 'twitter_text',  'sender_id', 'sender_screen_name', 'sender_name', 'sender_avatar', 'created_on']
