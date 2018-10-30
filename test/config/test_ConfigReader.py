# -*- coding: utf-8 -*-
"""
    tests.config.test_ConfigReader
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services_commons.config import ConfigParams
from pip_services_commons.run import Parameters
from pip_services_components.config import ConfigReader

#todo
# class TestConfigReader():
#     def test_parameterize(self):
#         config = "{{#if A}}{{B}}{{/if}}"
#         values = Parameters.from_tuples("A", "true",
#                                         "B", "XYZ")
#         parameters = ConfigParams()
#         parameters.append(values)
#         reader = ConfigReader()
#
#         assert "XYZ" == reader._parameterize(config, parameters)