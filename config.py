from airflow import configuration as conf

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URI = conf.get('core', 'SQL_ALCHEMY_CONN')

# Configuración de autenticación
AUTH_ROLE_PUBLIC = 'Public'
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Public'
AUTH_ROLE_ADMIN = 'Admin'
AUTH_USER_REGISTRATION_ROLE = 'Admin'

# Configuración de la seguridad
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SECRET_KEY = 'my_secret_key'
