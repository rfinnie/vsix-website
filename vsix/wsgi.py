# SPDX-PackageSummary: vsix-website
# SPDX-FileCopyrightText: Copyright (C) 2020-2025 Ryan Finnie
# SPDX-License-Identifier: MPL-2.0

"""
WSGI config for vsix project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vsix.settings")

application = get_wsgi_application()
