# -*- coding: utf-8 -*-
"""
    pip_services_commons.connect.DefaultDiscoveryFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Default discovery factory implementation

    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_components.info.ContextInfo import ContextInfo

class TestContextInfo:
    def test_name(self):
        context_info = ContextInfo()
#        assert context_info._name == "unknown"
#todo