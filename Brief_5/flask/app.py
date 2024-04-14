from flask import Flask, render_template, request
from forms import FilmForm
from models import load_model, predict_imdb_score

app = Flask(__name__)
app.config['SECRET_KEY'] = 'imdb'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FilmForm()
    if form.validate_on_submit():
        # Charger le modèle
        model = load_model()
        # Récupérer les données du formulaire
        data = [[
            form.duration.data,
            form.num_critic_for_reviews.data,
            form.actor_3_fb_likes.data,
            form.actor_1_fb_likes.data,
            form.num_voted_users.data,
            form.cast_total_fb_likes.data,
            form.facenumber_in_poster.data,
            form.num_user_for_reviews.data,
            form.actor_2_fb_likes.data,
            form.movie_fb_likes.data
        ]]
        # Faire une prédiction
        prediction = predict_imdb_score(model, data)
        return render_template('result.html', prediction=prediction[0])
    return render_template('index.html', form=form)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')
