
from twython import Twython
from twitter_stream.models import MonitorTwitter, GeoTwitter
import datetime


def collect_monitor_twitter():

    a_date_time_now = datetime.datetime.now()

    all_MonitorTwitter= MonitorTwitter.objects.filter(initial_date__gt=a_date_time_now , final_date__lte=a_date_time_now)

    for monitor_twitter in all_MonitorTwitter:

        collect_twitters(args=[monitor_twitter.id])



def collect_twitters(monitorTwitter_id):
    try:
        monitor_twitter = MonitorTwitter.objects.get(id=monitorTwitter_id)

    except MonitorTwitter.DoesNotExist:
        return

    twitter = Twython(monitor_twitter.app_key(), monitor_twitter.app_secret(), oauth_version=2)
    monitor_twitter.set_acess_token(twitter.obtain_access_token())
    twitter = Twython(monitor_twitter.app_key(), access_token=monitor_twitter.access_token)

    items = twitter.search(q=monitor_twitter.search_term, result_type='recent', count=100, since_id=monitor_twitter.since_id)
    if items:
        for item in items['statuses']:
            geo_twitter = GeoTwitter()
            geo_twitter.monitor_twitter = monitor_twitter
            geo_twitter.twitter_id = item['id']
            geo_twitter.twitter_text= item['text']
            geo_twitter.sender_id = item['user']['id']
            geo_twitter.sender_screen_name = item['user']['screen_name']
            geo_twitter.sender_name = item['user']['name']
            geo_twitter.sender_avatar = item['user']['profile_image_url']
            geo_twitter.geom = item['geo']
            geo_twitter.save()

        monitor_twitter.last_searched_date = datetime.datetime.now()
        monitor_twitter.since_id = items['search_metadata']['max_id']
        monitor_twitter.save()
