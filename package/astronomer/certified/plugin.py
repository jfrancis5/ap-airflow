from airflow.plugins_manager import AirflowPlugin
from astronomer.certified.blueprint import ACThemeBlueprint


class AstronomerCertifiedPlugin(AirflowPlugin):

    name = "astronomer_certified"

    flask_blueprints = [ACThemeBlueprint()]
