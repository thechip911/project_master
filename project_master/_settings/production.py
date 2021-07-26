"""
Production Environment
"""
SECRET_KEY = '_7qszfqu$p39=%it$-v_&$_22+9i*^m!3t+k($osi3n5&q9lu='

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project_management',
        'USER': 'project_management',
        'PASSWORD': 'project_management',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
