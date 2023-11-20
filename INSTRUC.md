# Installation Guide for new Virtual Env
## 1: Create virtual environment:
python3 -m venv venv

## 2: Activate venv (MAC):
source venv/bin/activate

## 3: Install packages in the venv:

### Flask
pip install Flask, Flask_SQLAlchemy, Flask-Bcrypt, Flask-JWT-Extended, Flask-Cors

### Vue CLI 
npm install -g @vue/cli
OR
sudo npm install -g @vue/cli

### Vue related
npm install axios vuex vue-router

### Bootstrap
npm install bootstrap
npm i bootstrap-icons

# Running the application:

## 1: Activate venv (MAC)
source venv/bin/activate

## 2: Terminals
Open two terminals:
One for running app.py
One for backend

### Frontend terminal run:
cd frontend
npm run serve

### Backend terminal run:
python run.py
