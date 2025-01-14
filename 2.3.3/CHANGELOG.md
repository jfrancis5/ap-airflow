# Changelog

Astronomer Certified 2.3.3-1, 2022-07-11
----------------------------------------

User-facing CHANGELOG for AC 2.3.3+astro.1 from Airflow 2.3.3:

### Bugfixes

- Fix zombie task handling with multiple schedulers ([#24906](https://github.com/apache/airflow/pull/24906))
- TriggerDagRunOperator.operator_extra_links is attr ([#24676](https://github.com/apache/airflow/pull/24676))
- [astro] seed log_template table (#1497) ([commit](https://github.com/astronomer/airflow/commit/6d80ff139d07746991653eee682601d04b94ad74))
- [astro] Reconcile orphan holding table handling ([commit](https://github.com/astronomer/airflow/commit/ce1708d0aadba792a977db82c585776f4fee672e))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/c42ed38f590be13c4ebae2634d83f674e45d394b))
- [astro] Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/b9436bb013d8fd02f4f83ba00c56df32a89270ea))
