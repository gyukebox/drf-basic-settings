import os
import glob
from split_settings.tools import include

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['PROJECT_SECRET_KEY']

ENV = os.environ.get('PROJECT_ENV', 'development')

COMPONENTS_DIR = os.path.join(BASE_DIR, 'project', 'settings', 'components')

COMPONENTS = [
    'components/{}'.format(os.path.basename(component))
    for component in glob.glob(os.path.join(COMPONENTS_DIR, '*.py'))
]
ENVIRONMENTS = ['environments/{}.py'.format(ENV)]

SETTINGS = COMPONENTS + ENVIRONMENTS

include(*SETTINGS)
