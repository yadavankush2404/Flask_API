from flask import Flask,jsonify
import os
from .auth import auth
from .bookmarks import bookmark
from .database import db

def create_app(test_config=None): 
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY = os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DB_URI"),
            # SQLALCHEMY_TRACK_MODIFICATIONS = False
        )
    else:
        app.config.from_mapping(test_config)
    
    @app.get("/")
    def index():
        return "hello world"

    @app.get("/hello")
    def say_hello():
        return jsonify({"message": "Hello World!!"})
    
    # if __name__=="__main__":
    #     app.run(debug=True)
    db.app=app
    db.init_app(app)
    app.app_context().push()
    app.register_blueprint(auth)
    app.register_blueprint(bookmark)

    return app 

# if __name__=="__main__":
    # app = create_app()
#     app.run(debug=True)

# to run the app type flask run in the terminal and do not run the file directly because relative imports have been made and that can cause error
