import os

from .base import *  # noqa: F403, F401

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

ALLOWED_HOSTS = []  # TODO: djangoindia domain goes here

ADMIN_URL = os.environ.get("DJANGO_ADMIN_URL")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# AWS settings
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

# Media files (Images, etc.)
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "AWS_ACCESS_KEY_ID": AWS_ACCESS_KEY_ID,
            "AWS_SECRET_ACCESS_KEY": AWS_SECRET_ACCESS_KEY,
            "AWS_STORAGE_BUCKET_NAME": AWS_STORAGE_BUCKET_NAME,
            "AWS_S3_REGION_NAME": AWS_S3_REGION_NAME,
        },
    },
    "staticfiles": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
        "LOCATION": STATIC_ROOT,
    },
}
