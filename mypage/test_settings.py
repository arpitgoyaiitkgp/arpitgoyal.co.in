from mypage.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite_database',
        'HOST': '127.0.0.1',
        'USER': os.environ.get('MYSITE_SQL_USER', ''),
        'PASSWORD': os.environ.get('MYSITE_SQL_PASSWORD', ''),
    }
}
