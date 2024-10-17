from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from config import Config
from routes import auth, stations, users, analyses

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

# Importa as rotas
app.register_blueprint(auth.bp)
app.register_blueprint(stations.bp)
app.register_blueprint(users.bp)
app.register_blueprint(analyses.bp)

if __name__ == '__main__':
    app.run(debug=True)
