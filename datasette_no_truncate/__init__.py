from datasette import hookimpl


@hookimpl
def render_cell(value):
    if isinstance(value, str):
        return value
