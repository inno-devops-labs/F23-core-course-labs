from flask import Response, Blueprint
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, CollectorRegistry, Counter

metrics_blueprint = Blueprint('metrics', __name__)

registry = CollectorRegistry()

http_request_total = Counter('http_requests_total', 'Numer of HTTP requests', registry=registry)


@metrics_blueprint.before_app_request
def increment_request_counter():
    """Middleware to count number of http requests"""
    http_request_total.inc()


@metrics_blueprint.route('/metrics')
def metrics():
    """Implementation of GET request for prometheus metrics"""
    return Response(generate_latest(registry), content_type=CONTENT_TYPE_LATEST)
