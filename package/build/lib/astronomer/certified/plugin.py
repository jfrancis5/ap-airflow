from airflow.plugins_manager import AirflowPlugin
from astronomer.certified.blueprint import ACThemeBlueprint

from airflow.plugins_manager import AirflowPlugin

class AstronomerCertifiedPlugin(AirflowPlugin):

    name = "astronomer_certified_extensions"

    flask_blueprints = [ACThemeBlueprint()]
