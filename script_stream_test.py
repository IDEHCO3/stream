from twitter_stream_api.models import MonitorTwitter
from twitter_stream_api.tasks import twitt_py

monitorTwitter = MonitorTwitter.objects.get(id=7)
twittpy = twitt_py(monitorTwitter)
items = twittpy.search(q=monitorTwitter.search_term, result_type='recent', count=100, since_id=monitorTwitter.since_id)