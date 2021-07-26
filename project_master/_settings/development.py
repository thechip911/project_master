"""
Development Environment
"""
SECRET_KEY = '_7qszfqu$p39=asdfit$-v_&$_2245i*^m!3t+k($osi3n5&q9lu='

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project_management_development',
        'USER': 'project_management_development',
        'PASSWORD': 'project_management_development',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
