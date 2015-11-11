from celery import task
from twython import Twython
from twitter_stream.models import MonitorTwitter, GeoTwitter
import datetime



@task(ignore_result=True)
def collect_monitor_twitter():

    a_date_time_now = datetime.datetime.now()

    all_MonitorTwitter= MonitorTwitter.objects.filter(initial_date__gt=a_date_time_now , final_date__lte=a_date_time_now)

    for monitor_twitter in all_MonitorTwitter:

        collect_twitters.apply_async(args=[monitor_twitter.id])


#@task(ignore_result=True)
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
            geo_twitter.social_item_id = item['id']
            geo_twitter.social_item_text = item['text']
            geo_twitter.social_user_id = item['user']['id']
            geo_twitter.social_user_screen_name = item['user']['screen_name']
            geo_twitter.social_user_name = item['user']['name']
            geo_twitter.social_user_avatar = item['user']['profile_image_url']
            geo_twitter.save()

        monitor_twitter.last_searched_date = datetime.now()
        monitor_twitter.since_id = items['search_metadata']['max_id']
        monitor_twitter.save()
