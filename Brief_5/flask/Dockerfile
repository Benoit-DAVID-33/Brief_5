FROM python:slim-bullseye
LABEL version=v1.0.0
LABEL app=shane-app

ENV FLASK_APP=app.py
ENV FLASK_ENV=dev

# Définir le répertoire de travail
WORKDIR /app
# Copier les fichiers de l'application
COPY . /app
RUN pip install -r /app/requirements.txt
# Exposer le port
EXPOSE 5000

# Copier le fichier du modèle dans le conteneur Docker
COPY random_forest_model.pkl /app/random_forest_model.pkl

# Mettre à jour les packages Python
RUN pip install --upgrade pip && \
    pip install --upgrade -r requirements.txt

# Démarrez l'application
CMD ["python", "app.py", "--host=0.0.0.0"]

