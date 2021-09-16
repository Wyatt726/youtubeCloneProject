SECRET_KEY = 'django-insecure-^u!q@so5p1y2fb4(2agz)cr0lsd98%6!#+(b5#mc!8ff^_f@6d'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone1',
        'USER': 'root',
        'PASSWORD': 'Number11',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}