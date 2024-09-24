import home
from .settings import project

home.home.add_url_rule(rule = "/", view_func= home.render_home)
project.register_blueprint(blueprint=home.home)
