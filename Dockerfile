# SPDX-PackageSummary: vsix-website
# SPDX-FileCopyrightText: Copyright (C) 2020-2025 Ryan Finnie
# SPDX-License-Identifier: MPL-2.0
FROM python:3.12

COPY . /tmp/build
RUN pip install --no-cache-dir '/tmp/build[gunicorn]' && useradd -ms /bin/bash app && rm -rf /tmp/build

ENV DJANGO_SETTINGS_MODULE="vsix.settings"
USER app
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "-k", "gthread", "--error-logfile", "-", "--capture-output", "vsix.wsgi:application" ]
EXPOSE 8000/tcp
