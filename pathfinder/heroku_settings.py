from pathfinder.settings import *
import os

import django_heroku

DEBUG = False

# clintion fix:
# DEBUG = os.getenv('DEBUG', False)

django_heroku.settings(locals())