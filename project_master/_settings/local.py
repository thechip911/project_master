"""
Local Environment
"""


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6=zV!6y($4h_JQ7xpLJwq[acipi0f3c<MJo~oc$u^4?6G-DBMt46Ljw^73:A3NZ'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'product_master_local',
        'USER': 'product_master_local',
        'PASSWORD': 'product_master_local',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
