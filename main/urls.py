import user_page

from .settings import project

user_page.user.add_url_rule(rule='/user/', view_func=user_page.render_user)
project.register_blueprint(blueprint=user_page.user)