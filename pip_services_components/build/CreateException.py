# -*- coding: utf-8 -*-
"""
    pip_services_common.build.CreateException
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Create exception type
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_commons.errors.InternalException import InternalException
from pip_services_commons.refer import ReferenceException


class CreateException(InternalException):
    """
    Exception thrown when component cannot be created by a factory
    """

    def __init__(self, correlation_id = None, message = None):
        super(ReferenceException, self).__init__(correlation_id, "CANNOT_CREATE", message)
