alembic upgrade head
echo $1
alembic revision --autogenerate -m "$1"

