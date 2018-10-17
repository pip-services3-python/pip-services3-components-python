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

    def from_config(self, config):
        value = ContextInfo()
        value.configure(config)
        return value
