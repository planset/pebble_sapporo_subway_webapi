# -*- coding: utf-8 -*-
from django.core.serializers.json import Serializer as JSONSerializer

class Serializer(JSONSerializer):
    def get_dump_object(self, obj):
        return self._current

    def start_serialization(self):
        super(Serializer, self).start_serialization()
        self.json_kwargs["ensure_ascii"] = False
