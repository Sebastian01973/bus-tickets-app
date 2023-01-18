from django.db import connection


def execute_query(query, params):
    """
    Executes the given query and returns the data in the form of a dictionary
    """
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        columns = [col[0] for col in cursor.description]
        values = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return values
