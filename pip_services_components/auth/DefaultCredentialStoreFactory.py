# -*- coding: utf-8 -*-
"""
    pip_services_commons.auth.DefaultCredentialStoreFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Default credential store factory implementation
    
    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .MemoryCredentialStore import MemoryCredentialStore

from pip_services_commons.refer.Descriptor import Descriptor
from ..build.Factory import Factory

DefaultCredentialStoreFactoryDescriptor = Descriptor(
    "pip-services", "factory", "credential-store", "default", "1.0"
)

MemoryCredentialStoreDescriptor = Descriptor(
    "pip-services", "credential-store", "memory", "*", "1.0"
)

class DefaultCredentialStoreFactory(Factory):
    """
    Creates ICredentialStore components by their descriptors.
    """
    def __init__(self):
        """
        Create a new instance of the factory.
        """
        self.register_as_type(MemoryCredentialStoreDescriptor, MemoryCredentialStore)
