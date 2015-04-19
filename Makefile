PYTHON=`which python`
DESTDIR=/

lift:
	$(PYTHON) manage.py runserver localhost:3333

shell:
	$(PYTHON) ./manage.py shell
