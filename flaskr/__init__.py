import os
from flask import Flask


def create_app(test_config=None):
    """This function is known as the application factory. Any configuration, registration, and other setup the
    application needs will happen inside the function, then the application will be returned."""

    # the flask app needs to know where it is located to set up some paths
    app = Flask(import_name=__name__, instance_relative_config=True)
    # app.instance_path = "../instance"
    # The instance folder is designed to not be under version control and be deployment specific.
    # It’s the perfect place to drop things that change at runtime, configuration files and database files
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(mapping=test_config)  # use test_config for testing purpose

    try:
        os.makedirs(name=app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello World!"

    from . import db, auth, blog
    db.init_app(app=app)
    app.register_blueprint(auth.blue_print)

    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app


if __name__ == "__main__":
    create_app()