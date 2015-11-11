from django.contrib.gis.db import models

from django.utils.datetime_safe import datetime

from stream.settings import AUTH_USER_MODEL


# Create your models here.
class AccountTwitter(models.Model):

    user = models.OneToOneField(AUTH_USER_MODEL, related_name='account_twitter')
    consumer_key = models.CharField(max_length=100, null=True, blank=True)
    consumer_secret = models.CharField(max_length=100, null=True, blank=True)
    consumer_token = models.CharField(max_length=100, null=True, blank=True)
    consumer_token_secret = models.CharField(max_length=100, null=True, blank=True)


class MonitorTwitter(models.Model):

    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name='User', related_name='col_of_monitor_twitter')
    search_term = models.CharField( 'Search term',  max_length=100, null=True)
    name = models.CharField( 'Name',  max_length=100, unique=True)
    description = models.CharField( 'Description',  max_length=300, null=True)
    initial_date = models.DateTimeField(default=datetime.now)
    final_date = models.DateTimeField(default=datetime.now)
    last_searched_date=models.DateTimeField(null=True)
    interval = models.CharField(help_text='hh:mm:ss', default='01:00:00', max_length=8)
    since_id = models.BigIntegerField('Since id', default=0, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    access_token = None

    def account_twitter(self):
        at_list = AccountTwitter.objects.filter(user_id=self.user.id)
        if at_list:
            return at_list[0]
        return None

    def app_key(self):
        account = self.account_twitter()
        if account is not None:
            return account.consumer_key
        return None

    def app_secret(self):
        account = self.account_twitter()
        if account is not None:
            return self.user.account_twitter.consumer_secret
        return None

    def set_acess_token(self,a_access_token):
        self.access_token = a_access_token


class GeoTwitter(models.Model):

    monitor_twitter = models.ForeignKey(MonitorTwitter, related_name='geotwitters' )
    twitter_id = models.CharField('Twitter id', max_length=50, null=True)
    twitter_text = models.TextField('twitter text', max_length=50, null=True)
    sender_id = models.CharField('sender id', max_length=50, null=True)
    sender_screen_name = models.CharField('Sender scream name', max_length=50, null=True)
    sender_name = models.CharField('sender Name', max_length=100, null=True)
    sender_avatar = models.URLField('Sender Avatar ', max_length=250, null=True )
    created_on = models.DateTimeField(auto_now_add=True)

    geom = models.PointField(blank=True, null=True)


