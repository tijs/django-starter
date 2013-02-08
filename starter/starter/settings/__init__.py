from __future__ import absolute_import
import os
"""
Use the production settings if PRODUCTION environment variable is set,
else use the local settings.
"""
if 'PRODUCTION' in os.environ:
    from .production import *
else:
    try:
        from .local import *
    except ImportError:
        from .base import *