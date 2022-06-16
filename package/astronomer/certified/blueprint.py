import os
import airflow
from airflow.utils.log.logging_mixin import LoggingMixin

from flask import Blueprint

def get_versions():
    try:
        airflow_version = airflow.__version__
        airflow_upstream_version = airflow_version.split('.dev')[0].split('+astro')[0]
        ac_url_version = airflow_upstream_version.replace('.', '-')
    except Exception:
        airflow_version = None
        airflow_upstream_version = None
        ac_url_version = None
    try:
        import importlib_metadata
    except ImportError:
        from importlib import metadata as importlib_metadata

    try:
        ac_version = importlib_metadata.version('astronomer-certified')
    except importlib_metadata.PackageNotFoundError:
        # Try to work out ac_version from airflow version
        if airflow_version:
            ac_version = airflow_version.replace('+astro.', '-')
        else:
            ac_version = None
    return ac_version, airflow_upstream_version, ac_url_version


class ACThemeBlueprint(Blueprint, LoggingMixin):

    airflow_base_template = None

    def __init__(self):

        super().__init__(
            "astronomer_certified",
            __name__,
            static_folder="static",
            template_folder=os.path.join(os.path.dirname(__file__), "templates"),
        )

    def new_template_vars(self):
        ac_version, airflow_upstream_version, ac_url_version = get_versions()
        return {
            "airflow_base_template": self.airflow_base_template,
            'ac_version': ac_version,
            'airflow_upstream_version': airflow_upstream_version,
            'ac_url_version': ac_url_version,
        }

    def register(self, app, options, first_registration):
        """
        Re-configure Flask to use our customized layout (that includes the call-home JS)
        Called by Flask when registering the blueprint to the app
        """

        # Don't run if we're not at appbuilder stage yet
        if not hasattr(app, "appbuilder"):
            return

        # Change documentation menu if needed
        app.appbuilder.add_link(
            name="Astronomer",
            label="Astronomer Docs",
            href='https://www.astronomer.io/docs',
            category="Astronomer",
        )
        app.appbuilder.add_link(
            name="Astronomer",
            label="Astronomer Registry",
            href='https://registry.astronomer.io',
            category="Astronomer",
        )
        app.appbuilder.add_link(
            name="Astronomer",
            label="Airflow Guides",
            href='https://www.astronomer.io/guides',
            category="Astronomer",
        )

        # Change base template if needed
        self.airflow_base_template = app.appbuilder.base_template
        if app.appbuilder.base_template in ["airflow/master.html", "airflow/main.html"]:
            app.appbuilder.base_template = "certified_base.html"
        else:
            self.log.warning(
                "Not replacing appbuilder.base_template, it didn't have the expected value. Update"
                " available messages will not be visible in UI"
            )

        # Let us inject variables into the Jinja context
        self.app_context_processor(self.new_template_vars)

        super().register(app, options, first_registration)