from flask import Flask
from routes.auth import auth_bp
from routes.contributions import contributions_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(contributions_bp)

if __name__ == "__main__":
    app.run(debug=True)
