from flask import Flask, request, render_template
import utils, templates

app = Flask(__name__)

@app.route('/')
def all_candidates():
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:idx>')
def candidate_by_pk(idx):
    candidate = utils.get_candidate(idx)
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>/')
def search(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)

@app.route('/skill/<skill_name>')
def candidates_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('search.html', skill_name=skill_name, candidates=candidates)


app.run('0.0.0.0', 8000)