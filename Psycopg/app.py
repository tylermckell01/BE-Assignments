from flask import Flask
import os

import routes
from db import create_all

app_host = os.environ.get('APP_HOST')
app_port = os.environ.get('APP_PORT')

app = Flask(__name__)

app.register_blueprint(routes.product)
app.register_blueprint(routes.companies)
app.register_blueprint(routes.categories)


if __name__ == '__main__':
    create_all()
    app.run(host='0.0.0.0', port='8086')