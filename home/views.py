import flask

def render_home():
  flask.render_template(template_name_or_list="home.html")