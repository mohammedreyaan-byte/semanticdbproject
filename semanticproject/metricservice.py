from django.db import connection
from .properties.metrics import METRICS
from .properties.semantic import SEMANTIC_MODEL

#Metric Calculator Function:

def calculate_metric(metric_name):

    metric = METRICS[metric_name]
    field_name = metric["field"]
    aggregation = metric["aggregation"]

    if field_name not in SEMANTIC_MODEL["book"]["dimensions"]:
        raise ValueError(f"Field {field_name} does not exist")

    column = SEMANTIC_MODEL["book"]["dimensions"][field_name]["column"]
    table = SEMANTIC_MODEL["book"]["table"]

    query = f"""
    SELECT {aggregation}({column}) FROM {table}
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchone()
        return results[0]
