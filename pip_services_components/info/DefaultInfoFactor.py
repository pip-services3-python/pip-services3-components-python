# -*- coding: utf-8 -*-
"""
    pip_services_commons.connect.DefaultDiscoveryFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Default discovery factory implementation

    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_commons.refer.Descriptor import Descriptor
from ..build.Factory import Factory
from .ContextInfo import ContextInfo

Descriptor = Descriptor("pip-services", "factory", "info", "default", "1.0");
ContextInfoDescriptor = Descriptor("pip-services", "context-info", "default", "*", "1.0");
ContainerInfoDescriptor =  Descriptor("pip-services", "container-info", "default", "*", "1.0");

class DefaultInfoFactory(Factory):

    def __init__(self):
        self.register_as_type(ContextInfoDescriptor, ContextInfo)
        self.register_as_type(ContainerInfoDescriptor, ContextInfo)