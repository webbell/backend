def create_app(app):
    from .cli import register
    register(app)
