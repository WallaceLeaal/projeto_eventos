from flask import Flask
from extensions import db
from controllers.evento_controller import evento_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eventos.db"

db.init_app(app)
app.register_blueprint(evento_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)