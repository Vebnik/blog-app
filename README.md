# How to launch

### Manual
- install `uv` manager for python
- clone this repo `git clone this-repo`
- install deps `uv sync`
- preapre some database (sqlite3, etc.)
- create `.env` since from `.env.template`
- make migrations `uv run py .\manage.py migrate`
- run dev server `uv run py .\manage.py runserver`

### Docker
- run `docker compose -p blog-app-cluster up -d`