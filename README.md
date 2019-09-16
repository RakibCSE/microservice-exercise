# microservice-exercise

## Instructions to run the script

1. Goto the directory where you want to store your project.
2. Clone the git repository to the project directory.
3. Open the terminal and navigate to the project directory from the terminal.
4. Create virtual environment from the terminal by typing ```virtualenv .env``` and activate it by typing `source .env/bin/activate`(for Linux), `.env\Scripts\activate`(for Windows).
    * If you don't have `virtualenv` installed then install it by typing `pip install virtualenv`.
5. Install the project dependencies by typing `pip install -r requirements.txt` on the terminal.
6. Create `config.local.json` file with the same content of `config.json` file.
7. Migrate the database by typing `python manage.py makemigrations` and then `python manage.py migrate` on the terminal.
8. Create admin user if you want by typing `python manage.py createsuperuser` and give the required credentials on the terminal.
9. Now, Run the project from your **localhost** by typing `python manage.py runserver`
10. You can terminate the server anytime by **CTRL+c**.

### URL's I've implemented:

* /api/categories/
* /api/games
* /api/game/**id**/
* /admin/

**N:B:** *Replace `id` with the game id*
