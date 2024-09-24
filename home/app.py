import flask

home = flask.Blueprint(
  name = "Home",
  import_name= "home",
  template_folder= "templates"
)