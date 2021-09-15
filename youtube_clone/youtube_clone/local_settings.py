SECRET_KEY = 'django-insecure-h41h2_m1p2hty1(w7)=4zdoh6q@baw$#+w3de=co-%cspd=kvo'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone',
        'USER': 'root',
        'PASSWORD': 'Number11',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS':{
            'autocommit:True'
        }

    }
}
