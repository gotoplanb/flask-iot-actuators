## Setup

1. Create a directory
2. Install pipenv via `brew install pipenv`
3. Create a new environment with `pipenv --python 3.6`
4. Install dependences: `pipenv install Flask`
5. Start the enviornment with `pipenv shell` 

## Running
1. Start the server: `FLASK_APP=fan.py flask run`
2. View in browser: `http://127.0.0.1:5000/fan?speed=low`
3. Deactivate environment when finished: `exit`
 