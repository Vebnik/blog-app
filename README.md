# How to launch

### Manual
- install `uv` manager for python
- clone this repo `git clone this-repo`
- install deps `uv sync`
- preapre some database (sqlite3, etc.)
- create `.env` since from `.env.template`
- make migrations `uv run py .\manage.py migrate`
- preapre start data `uv run py .\manage.py prepare`
- run dev server `uv run py .\manage.py runserver`

### Docker
- clone this repo `git clone this-repo`
- run `docker compose -p blog-app up --build -d`

### Notes
After start we have basic admin user with creds

```plain
name:           admin
password:       admin
```

App availible on
```
admin panel:    http://localhost:8000/admin/
api interface:  http://localhost:8000/api-auth/login/
api root:       http://localhost:8000/api/
```

After start we have test data in database
```
post model:     100 records
comment:        1000 record (10 comments per each post)
```