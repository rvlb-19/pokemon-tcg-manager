# Pokémon TCG Manager

A simple application to manage your Pokémon TCG cards collection (under construction).

## How to use

1. Download this repository and install the dependencies.

2. Then, run `python manage.py migrate`.

3. Create a superuser using `python manage.py createsuperuser` and then `python manage.py runserver`.

4. Go to `localhost:8000/admin` and log into the admin panel.

5. Choose a Collection to add to the database. Doing this will automagically import all cards from the chosen collection.

6. Access the Cards menu to view the newly added data.

## Credits

This application was developed using data consumed from the awesome (Pokémon TCG API)[https://github.com/PokemonTCG/pokemon-tcg-api].

Pokémon and Pokémon character names are trademarks of Nintendo.

This application was developed with studying purposes and cannot be commercialized.