"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()


# ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.classifier.random_forest import RandomForestClassifier

try :
    registry = MLRegistry() # Create ML regi
    rf = RandomForestClassifier()
    # add to ML regi
    registry.add_algorithm(endpoint_name="classifier",
                           algorithm_object=rf,
                           algorithm_name="random forest",
                           algorithm_status="testing",
                           algorithm_version="0.0.1",
                           owner="Jeong Seok Han",
                           algorithm_description="testing",
                           algorithm_code = inspect.getsource(RandomForestClassifier))
except Exception as e:
    print("레지스트리에 알고리즘을 불러오는데 예외가 발생했습니다.", str(e))