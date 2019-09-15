import requests
import logging

if __name__ == '__main__':

    # these two lines enable debugging at httplib level (requests->urllib3->httplib)
    # you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
    # the only thing missing will be the response.body which is not logged.
    import httplib

    httplib.HTTPConnection.debuglevel = 0
    logging.basicConfig()  # you need to initialize logging, otherwise you will not see anything from requests
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests.get('http://httpbin.org/headers')
