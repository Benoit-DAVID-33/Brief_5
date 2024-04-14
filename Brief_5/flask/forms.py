from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class FilmForm(FlaskForm):
    num_critic_for_reviews = FloatField('Nombre de critiques pour la revue', validators=[DataRequired()])
    duration = FloatField('Durée (en minutes)', validators=[DataRequired()])
    actor_3_fb_likes = FloatField('Likes Facebook de l\'acteur 3', validators=[DataRequired()])
    actor_1_fb_likes = FloatField('Likes Facebook de l\'acteur principal', validators=[DataRequired()])
    num_voted_users = FloatField('Nombre d\'utilisateurs votants', validators=[DataRequired()])
    cast_total_fb_likes = FloatField('Total des likes Facebook pour le casting', validators=[DataRequired()])
    facenumber_in_poster = FloatField('Nombre de visages dans l\'affiche', validators=[DataRequired()])
    num_user_for_reviews = FloatField('Nombre d\'utilisateurs pour les revues', validators=[DataRequired()])
    actor_2_fb_likes = FloatField('Likes Facebook de l\'acteur 2', validators=[DataRequired()])
    imdb_score = FloatField('Note IMDb', validators=[DataRequired()])
    movie_fb_likes = FloatField('Likes Facebook du film', validators=[DataRequired()])
    
    submit = SubmitField('Prédire la note IMDb')
