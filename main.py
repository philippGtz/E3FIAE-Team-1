from flask import Flask
import index
from config import Config 

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(index.bp_index)

if __name__ == '__main__':
  app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])
  print('Start aus Entwicklungsumgebung')
else:
  print('Start von Webserver')