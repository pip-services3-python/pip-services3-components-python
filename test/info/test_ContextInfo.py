# -*- coding: utf-8 -*-
"""
    pip_services_commons.connect.DefaultDiscoveryFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Default discovery factory implementation

    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest
import datetime

from pip_services_commons.config import ConfigParams
from pytz import timezone

from pip_services_components.info.ContextInfo import ContextInfo

class TestContextInfo:
    def test_name(self):
        context_info = ContextInfo("unknown")
        assert context_info._name == "unknown"

        update = "new name"
        context_info._name = update
        assert context_info._name == "new name"

    def test_description(self):
        context_info = ContextInfo()
        assert context_info._description == None

        update = "new description"
        context_info._description = update
        assert context_info._description == "new description"

    def test_context_id(self):
        context_info = ContextInfo()
        assert context_info.context_id == None

        update = "new context_id"
        context_info.context_id = update
        assert context_info.context_id == "new context_id"

    def test_start_time(self):
        context_info = ContextInfo()
        now = datetime.datetime.now()
        assert context_info.start_time.year == now.year
        assert context_info.start_time.month == now.month

        context_info.start_time = datetime.datetime(1975, 4, 8)
        assert context_info.start_time.year == 1975
        assert context_info.start_time.month == 4
        assert context_info.start_time.day == 8

    def test_from_config(self):
        config = ConfigParams.from_tuples("name", "new name",
                                          "description", "new description",
                                          "properties.access_key", "key",
                                          "properties.store_key", "store key")
        context_info = ContextInfo.from_config(config)
        assert context_info._name == "new name"
        assert context_info._description == "new description"