# SPDX-PackageSummary: vsix-website
# SPDX-FileCopyrightText: Copyright (C) 2020-2025 Ryan Finnie
# SPDX-License-Identifier: MPL-2.0

import hashlib
import hmac
import ipaddress
import time

from django.http import HttpResponse
from django.template import loader

from .settings import BASE_DOMAIN, SECRET_KEY
from .werder import get_werder_werds


def get_randid():
    return get_werder_werds(1)[0]


def index_commandline(request):
    now = int(time.time())
    now_epoch = now - (now % 20826)
    access_key = hmac.new(
        SECRET_KEY.encode("UTF-8"),
        msg=str(now_epoch).encode("UTF-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()[0:4]

    server_hostname = request.get_host()

    context = {
        "access_key": access_key,
        "base_domain": BASE_DOMAIN,
        "randid": get_randid(),
        "server_hostname": server_hostname,
    }

    if request.GET.get("a", "") == access_key:
        template = loader.get_template("vsix/commandline.txt")
    else:
        template = loader.get_template("vsix/commandline_noauth.txt")
    response = HttpResponse(template.render(context, request), content_type="text/plain")
    response["Cache-control"] = "no-cache"
    response["Expires"] = "0"
    return response


def index(request):
    user_agent = request.META.get("HTTP_USER_AGENT", "")
    for m in ("curl/", "wget/", "lwp-request/", "libwww-perl/"):
        if m in user_agent:
            return index_commandline(request)

    ip = ipaddress.ip_address(request.META["REMOTE_ADDR"])
    server_hostname = request.get_host()

    forced_ipv4_host = False
    for h in ("4", "ipv4", "four"):
        if server_hostname == "{}.{}".format(h, BASE_DOMAIN):
            forced_ipv4_host = True
            break

    if ip.exploded.startswith("2001:0470:"):
        known_net = "he"
    else:
        known_net = None

    template = loader.get_template("vsix/index.html")
    context = {
        "base_domain": BASE_DOMAIN,
        "forced_ipv4_host": forced_ipv4_host,
        "is_ipv6": (ip.version == 6),
        "known_net": known_net,
        "randid": get_randid(),
        "server_hostname": server_hostname,
    }
    response = HttpResponse(template.render(context, request))
    response["Cache-control"] = "no-cache"
    response["Expires"] = "0"
    return response
