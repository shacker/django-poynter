"""
Settings and variables specific to the test runner.
"""

import os

import dj_database_url

from .settings import *  # noqa

if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.config()}

# DEBUG
# ------------------------------------------------------------------------------
# Turn debug off so tests run faster
DEBUG = False
TEMPLATES[0]["OPTIONS"]["debug"] = False  # noqa: F405
ENVIRONMENT = "test"

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = "CHANGEME!!!"  # noqa: S105

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

# In-memory email backend stores messages in django.core.mail.outbox
# for unit testing purposes
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"


# CACHING
# ------------------------------------------------------------------------------
# Speed advantages of in-memory caching without having to run Memcached.
# Commented out to ensure we are testing against actual redis backemnd from main settings.
# CACHES = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}

CACHEOPS_ENABLED = False

# Don't sleep when completing pluto_rt task
PLUTO_RT_CLEAR_DELAY = 0


# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = "django.test.runner.DiscoverRunner"


# PASSWORD HASHING
# ------------------------------------------------------------------------------
# Use fast password hasher so tests run faster
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# Override whitenoise static file server for tests
STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.StaticFilesStorage"  # noqa F405
CELERY_TASK_ALWAYS_EAGER = True

# Default in config.py, but local dev may have overriddenin local.yml. Tests should still use this.
GREENHOUSE_URL = "https://greenhouse-staging.energy-solution.net"

# Always use refresh instead of waiting
OPENSEARCH_REFRESH_DELAY = 0

# Assume test data does not have PII
# Decorate tests with @override_settings(SCRAMBLE_PII=True) to test the scramble functionality
SCRAMBLE_PII = False

OPENSEARCH_PREFIX = f"pytest{os.environ.get('PYTEST_XDIST_WORKER', '')}-"
