# djangoapp
Django Rest application

## Tests

pip install coverage 
coverage run --omit='*/venv/' manage.py test
coverage html

## API requests
curl -X POST -H "Content-Type: application/json" \
    -d '{"email": "user@domain.com", "password": "password"}' http://localhost:8080/api/token/
