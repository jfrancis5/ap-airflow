import functools
from airflow.plugins_manager import AirflowPlugin
from astronomer.certified.blueprint import ACThemeBlueprint
from astronomer.seed_log_template import seed_log_template

class AstronomerCertifiedPlugin(AirflowPlugin):

    name = "astronomer_certified_extensions"

    flask_blueprints = [ACThemeBlueprint()]

    @staticmethod
    def add_before_call(mod_or_cls, target, pre_fn):
        fn = getattr(mod_or_cls, target)

        @functools.wraps(fn)
        def run_before(*args, **kwargs):
            pre_fn()
            fn(*args, **kwargs)

        setattr(mod_or_cls, target, run_before)

    def on_load(cls, *args, **kwargs):
        # Borrowed concept from version_check plugin.
        # Seed the log template table before running the scheduler loop
        import airflow.jobs.scheduler_job
        cls.add_before_call(
        airflow.jobs.scheduler_job.SchedulerJob, '_run_scheduler_loop',
        seed_log_template
        )
