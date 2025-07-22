# SPDX-PackageSummary: vsix-website
# SPDX-FileCopyrightText: Copyright (C) 2020-2025 Ryan Finnie
# SPDX-License-Identifier: MPL-2.0

"""
ASGI config for vsix project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vsix.settings")

application = get_asgi_application()
