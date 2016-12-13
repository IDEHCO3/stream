from context_api.models import *

def context(model_class_name):
    dic = {}
    dic['geotwitters'] = {
        'twitter_id': {'@type': 'https://schema.org/Text', '@id':'https://schema.org/Integer'},
        'twitter_text': {'@type': 'https://schema.org/Text', '@id':'https://schema.org/Text'},
        'sender_id': {'@type': 'https://schema.org/Text', '@id':'https://schema.org/Integer'},
        'sender_screen_name': {'@type':'https://schema.org/Text', '@id':'https://schema.org/alternateName'},
        'sender_name': {'@type':'https://schema.org/Text', "@id": 'https://schema.org/name'},
        'sender_avatar': {'@type': '@id', '@id':'https://schema.org/Image'},
        'created_on': {'@type':'https://schema.org/DateTime', '@id': 'https://schema.org/dateCreated'},
        'geom': {'@type':'https://schema.org/geo', '@id':'https://schema.org/geo'}
    }

    for key in dic:
        classobj = Class(name=key, spatial='geometry')
        classobj.save()
        for key2 in dic[key]:
            context = dic[key][key2]
            Context(attribute=key2, means=context['@id'], type=context['@type'], classname=classobj).save()
