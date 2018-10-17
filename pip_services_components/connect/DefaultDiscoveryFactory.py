# -*- coding: utf-8 -*-
"""
    pip_services_commons.connect.DefaultDiscoveryFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Default discovery factory implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .MemoryDiscovery import MemoryDiscovery

from pip_services_commons.refer.Descriptor import Descriptor
from ..build.Factory import Factory

DefaultDiscoveryFactoryDescriptor = Descriptor(
    "pip-services", "factory", "discovery", "default", "1.0"
)

MemoryDiscoveryDescriptor = Descriptor(
    "pip-services", "discovery", "memory", "*", "1.0"
)

class DefaultDiscoveryFactory(Factory):

    def __init__(self):
        self.register_as_type(MemoryDiscoveryDescriptor, MemoryDiscovery)
