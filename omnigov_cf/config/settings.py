DEBUG = True

HELLO = 'OMNIGOV Connection Factory Management'

SERVER_NAME = 'localhost:8000'
SECRET_KEY = 'anysecretkey'

# Flask Mail
# MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'smtp.gmail.com')
# MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
# MAIL_PORT = os.getenv('MAIL_PORT', 587)
# MAIL_USE_TLS = bool(strtobool(os.getenv('MAIL_USE_TLS', 'true')))
# MAIL_USE_SSL = bool(strtobool(os.getenv('MAIL_USE_SSL', 'false')))
# MAIL_USERNAME = os.getenv('MAIL_USERNAME', None)
# MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', None)

# Celery.
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5
