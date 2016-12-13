from rest_framework.serializers import ModelSerializer
from context_api.context import ContextBase
from context_api.models import Context

class ContextSerializer(ContextBase):

    def __init__(self, classobject):
        super(ContextSerializer, self).__init__()

        for context in classobject.contexts.all():
            if context.type is not None:
                self.addAttribute(context.attribute, id=context.means, type=context.type)
            else:
                self.addAttribute(context.attribute, url=context.means)



