#!/bin/bash

. /opt/cn_p2_simple_ws/venv/bin/activate
export FLASK_APP="config"
export GUNICORN_CMD_ARGS='--bind=0.0.0.0 --access-logfile="-"'
flask db upgrade
exec gunicorn app:app