# SPDX-PackageName: vsix-website
# SPDX-PackageSupplier: Ryan Finnie <ryan@finnie.org>
# SPDX-PackageDownloadLocation: https://github.com/rfinnie/vsix-website
# SPDX-FileCopyrightText: © 2020 Ryan Finnie <ryan@finnie.org>
# SPDX-License-Identifier: MPL-2.0
FROM python:3.12

COPY . /tmp/build
RUN pip install --no-cache-dir '/tmp/build[gunicorn]' && useradd -ms /bin/bash app && rm -rf /tmp/build

ENV DJANGO_SETTINGS_MODULE="vsix.settings"
USER app
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "-k", "gthread", "--error-logfile", "-", "--capture-output", "vsix.wsgi:application" ]
EXPOSE 8000/tcp
