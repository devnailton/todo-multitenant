from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d3abte07zc4l1g(#5v4$&f!d4hfc_j4gl*ac*90d88tigg0%o3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

SHARED_APPS = (
    'django_tenants',          # Obrigatório
    'clientes',                # App com Cliente e Dominio
    'django.contrib.contenttypes', # Geralmente necessário no public
    # Remova admin, auth, sessions, messages, staticfiles daqui
)

TENANT_APPS = (
    # Apps essenciais do Django que rodam DENTRO de cada tenant
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes', # Pode estar aqui também
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Suas apps específicas de tenant
    'rest_framework',
    'tarefas',
)

# Esta linha continua igual, combinando as listas corretamente
INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

# Não se esqueça de definir o AUTH_USER_MODEL
AUTH_USER_MODEL = 'tarefas.Usuario'


MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',  # Deve ser primeiro
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True, # <--- GARANTA QUE ESTÁ TRUE
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configurações do Django Tenants
TENANT_MODEL = "clientes.Cliente"
TENANT_DOMAIN_MODEL = "clientes.Dominio"

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

WSGI_APPLICATION = 'app.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'todo',
        'USER': 'postgres',
        'PASSWORD': 'Nlt@@123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Cuiaba'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações adicionais do Django Tenants
PUBLIC_SCHEMA_NAME = 'public'
PUBLIC_SCHEMA_URLCONF = 'app.urls_public'