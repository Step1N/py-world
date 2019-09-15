import logging
import connexion
from flask_cors import CORS

log = logging.getLogger(__name__)


class APILogger:
    write = lambda message: log.debug(message)


class APIServer():
    def run_forever(self):
        app = connexion.FlaskApp(__name__)
        CORS(app.app)
        app.run(log=APILogger)


def start_api_server():
    APIServer().run_forever()


if __name__ == '__main__':
    start_api_server()
