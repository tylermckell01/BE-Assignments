import routes


def register_blueprints(app):
    app.register_blueprint(routes.product)
    app.register_blueprint(routes.categories)
    app.register_blueprint(routes.companies)
