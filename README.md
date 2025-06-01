# sm-words


## init
source .venv/bin/activate
pip install -r requirement.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 backup/import.py
python3 manage.py runserver