#!/bin/bash
set -e
python manage.py migrate --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell
echo 'Done!'
exit 0

