from flask import Flask
import index
from config import Config
from models import db
from items import initialize_database
import subprocess

app = Flask(__name__)

def get_git_info():
    try:
        commit_id = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')
        git_tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=1']).strip().decode('utf-8')
        return commit_id, git_tag
    except subprocess.CalledProcessError:
        return None, None

app.config.from_object(Config)

app.secret_key = app.config["SECRET_KEY"]

db.init_app(app)

app.register_blueprint(index.bp_index)

# Git-Informationen in den Context für alle Templates ansonsten müssten wir es in jeder Route einzeln übergeben zB 
#@app.route('/page1')
# def page1():
#     commit_id, git_tag = get_git_info()
#     return render_template('page1.html', commit_id=commit_id, git_tag=git_tag)
@app.context_processor
def inject_git_info():
    commit_id, git_tag = get_git_info()
    return dict(commit_id=commit_id, git_tag=git_tag)

if __name__ == '__main__':
  initialize_database(app)
  app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])
  print('Start aus Entwicklungsumgebung')
else:
  print('Start von Webserver')