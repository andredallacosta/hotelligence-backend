activate_env:
		bash -c "source env/bin/activate"

freeze_requirements:
		pip freeze > requirements.txt

run:
		python3 manage.py runserver

migrate:
		python3 manage.py makemigrations
		python3 manage.py migrate
