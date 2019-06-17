# Champ

Originally a workout generator made in Flask [(Code here)](https://github.com/broadsinatlanta/champ), it is now migrated over to Django and also extended with new features such as an API.
This project was initially my capstone project for Harvard's CS50 which was improved and extended! Check it out at [this site.](http://champ.atsushi.dev)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Installing

Using a virtual env (recommended), install dependancies from requirements.txt.

```
pip install -r requirements.txt
```
Then, just migrate the databases!
```
python manage.py migrate
```
Optional:
```
python manage.py createsuperuser
```

to use admin functionalities e.g. edit the database via the api.

Next you'd need to import the exercises themselves which can be found in the repo in workouts.helper.exercises_fin.csv.py.
The script read_exercises.py in the helpers directory can just be copy and pasted into a shell:

# In practice
Open a shell
```
python manage.py shell
```
and copy and paste the read_exercises.py contents into the shell.

# API
Champ comes with an API accessed by going to /api.
The schema can be seen at /api/schema.
There are two main models to see api/exercises/id & api/users/id.

## Deployment

To serve static files make sure [Whitenoise](http://whitenoise.evans.io/en/stable/django.html) is configured properly and run
```
python manage.py collectstatic
```

## TODO / Next steps:
* Migrate the database to MySQL / PostgreSQL

## Built With

* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework used
* [Bootstrap 4](https://v4-alpha.getbootstrap.com/) - CSS Frontend
* JQuery(https://jquery.com/) - UI/UX


## Authors

* **Me, Atsushi Toda** - [GitHub](https://github.com/broadsinatlanta) - [My personal website](https://www.atsushi.dev)

## License

This project is licensed under the MIT License.
