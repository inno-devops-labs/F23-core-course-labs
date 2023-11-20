"""
This module configures the BlackSheep application before it starts.
"""
from blacksheep import Application
from blacksheep_prometheus import use_prometheus_metrics

from app.docs import configure_docs
from app.errors import configure_error_handlers
from app.middlewares import configure_middlewares
from app.settings import Settings, load_settings


def configure_application(
    settings: Settings,
) -> Application:
    app = Application(show_error_details=settings.app.show_error_details)

    configure_error_handlers(app)
    configure_docs(app, settings)
    configure_middlewares(app)
    return app


app = configure_application(load_settings())
use_prometheus_metrics(app)
