# -*- coding: utf-8 -*-
"""
    pip_services_commons.counters.CachedCounters
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Cached counters implementation

    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import datetime
from pytz import timezone

from pip_services_commons.config.IReconfigurable import IReconfigurable

class ContextInfo(IReconfigurable):
    _name = "unknown"
    _properties = None
    _description = None
    context_id = None
    start_time = datetime.datetime.now()
    uptime = 0

    def __init__(self, name = None, description = None):
        self._name = name or "unknown"
        self._description = description

    def configure(self, config):
        self._name = config.get_as_string_with_default("name", self._name)
        self._name = config.get_as_string_with_default("info.name", self._name)

        self._description = config.get_as_string_with_default("description", self._description)
        self._description = config.get_as_string_with_default("info.description", self._description)

        self._properties = config.getSection("properties")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name if name != None else "unknown"

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_context_id(self):
        return self.context_id

    def set_context_id(self, context_id):
        self.context_id = context_id

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_uptime(self):
        return self.uptime

    def set_uptime(self, uptime):
        self.uptime = uptime

    def get_properties(self):
        return self._properties

    def set_properties(self, properties):
        self._properties = properties

    def from_config(self, config):
        value = ContextInfo()
        value.configure(config)
        return value
