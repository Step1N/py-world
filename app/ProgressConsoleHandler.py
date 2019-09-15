import logging
import requests
import logging.config


class CustomHandler(logging.StreamHandler):
    pass


logconfig = {
    'version': 1,
    'handlers': {
        'console': {
            'class': '__main__.CustomHandler',
        }
    },
    'loggers': {
        'custom': {
            'handlers': ['console'],
        }
    }
}

if __name__ == '__main__':
    logger = logging.getLogger('root')
    logger.setLevel('DEBUG')
    logging.config.dictConfig(logconfig)

    r = requests.get('http://httpbin.org/get?foo=bar&baz=python')
