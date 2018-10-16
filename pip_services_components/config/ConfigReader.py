# -*- coding: utf-8 -*-
"""
    pip_services_commons.config.CachedConfigReader
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Cached config reader implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pystache

from pip_services_commons.config import IConfigurable
from pip_services_commons.config import ConfigParams
from pip_services_components.config import IConfigReader

class ConfigReader(IConfigReader, IConfigurable):
    _parameters = None

    def __init__(self):
        self._parameters = ConfigParams()

    def configure(self, config):
        parameters = config.get_section("parameters")
        if len(parameters) > 0:
            self._parameters = parameters

    def read_config(self, correlation_id, parameters):
        raise NotImplementedError('Method is abstract and must be overriden')

    def _parameterize(self, config, parameters):
        parameters = self._parameters.override(parameters)
        return pystache.render(config, parameters)
