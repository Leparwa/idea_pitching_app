export SECRET_KEY="leresiSekjdskhdohsjd"

flask db init
flask db migrate -m "Initial Migration"
flask db upgrade
python3 manage.py server