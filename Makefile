activate_env:
		bash -c "source env/bin/activate"

freeze_requirements:
		pip freeze > requirements.txt

run:
		python manage.py runserver