
from .base import *
# LOCAL

SECRET_KEY='ovrny$2jc%ztbdihz%ob*k64za!$n(0pn8mj94m33@&-7%25ud'

#Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SYSTEM_EMAIL = 'yourname@example.com.com'
