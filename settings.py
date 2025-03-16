DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'masteruser_kvsi',
        'USER': 'masteruser',
        'PASSWORD': '3UlMqzhhrj1uYnijMuyKOrmJyMiNSjm5',
        'HOST': 'dpg-cvbe6jrtq21c73du621g-a.oregon-postgres.render.com',
        'PORT': '5432',
        'CONN_MAX_AGE': 60,  # Add connection age limit
        'OPTIONS': {
            'sslmode': 'require',  # Force SSL connection
        },
    }
}