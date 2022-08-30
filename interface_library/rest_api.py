'''
    GET     method is used to retrieve information from the given server using a given URI.
    POST	POST request method requests that a web server accepts the data enclosed in the body of the request message, most likely for storing it
    PUT	    PUT method requests that the enclosed entity be stored under the supplied URI. If the URI refers to an already existing resource, it is modified and if the URI does not point to an existing resource, then the server can create the resource with that URI.
    DELETE	The DELETE method deletes the specified resource
    HEAD	The HEAD method asks for a response identical to that of a GET request, but without the response body.
    PATCH	It is used for modify capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource

    Response object
    When one makes a request to a URI, it returns a response. This Response object in terms of python is returned by requests.method(), method being – get, post, put, etc. Response is a powerful object with lots of functions and attributes that assist in normalizing data or creating ideal portions of code. For example, response.status_code returns the status code from the headers itself, and one can check if the request was processed successfully or not.
    Response object can be used to imply lots of features, methods, and functionalities.

    response = requests.get('https://api.github.com/')

    response.headers	response.headers returns a dictionary of response headers.
    response.encoding	response.encoding returns the encoding used to decode response.content.
    response.elapsed	response.elapsed returns a timedelta object with the time elapsed from sending the request to the arrival of the response.
    response.close()	response.close() closes the connection to the server.
    response.content	response.content returns the content of the response, in bytes.
    response.cookies	response.cookies returns a CookieJar object with the cookies sent back from the server.
    response.history	response.history returns a list of response objects holding the history of request (url).
    response.is_permanent_redirect	response.is_permanent_redirect returns True if the response is the permanent redirected url, otherwise False.
    response.is_redirect	response.is_redirect returns True if the response was redirected, otherwise False.
    response.iter_content()	response.iter_content() iterates over the response.content.
    response.json()	    response.json() returns a JSON object of the result (if the result was written in JSON format, if not it raises an error).
    response.url	    response.url returns the URL of the response.
    response.text	    response.text returns the content of the response, in unicode.
    response.status_code	response.status_code returns a number that indicates the status (200 is OK, 404 is Not Found).
    response.request	response.request returns the request object that requested this response.
    response.reason	    response.reason returns a text corresponding to the status code.
    response.raise_for_status()	response.raise_for_status() returns an HTTPError object if an error has occurred during the process.
    response.ok	        response.ok returns True if status_code is less than 200, otherwise False.
    response.links	    response.links returns the header links.

    list of a ll the status codes 

    100 - Continue
    101 - Switching Protocols
    102 - Processing 
    103 - Early Hints

    200 - OK
    201 - Created
    202 - Accepted
    203 - Non-Authoritative information implemented since HTTP/1.1
    204 - No Content 
    205 - Reset content 
    206 - Partial content
    207 - Multi-Status
    208 - Already Reported
    226 - IM Used

    300 - Multiple Choices 
    301 - Moved Permanently
    302 - Found 
    303 - See Other
    304 - Not Modified 
    305 - Use Proxy 
    306 - Swtich Proxy
    307 - Temportary redirect
    308 - Permanent Redirect

    400 - Bad Request
    401 - Unauthorised
    402 - Payment Required 
    403 - Forbidden
    404 - Not Found 
    405 - Method Not Allowed
    406 - Not Acceptanble
    407 - Proxy Authentification Required 
    408 - Request Timeout
    409 - Conflict
    410 - Gone 
    411 - Lenght Required
    412 - Precondition
    413 - Payload too large
    414 - URI Too long
    415 - Unsupported Media Type
    416 - Range Not Satisfiable
    417 - Excpectation Failed
    421 - Misdirected Request
    422 - Unpocessable Entity
    423 - Locked 
    424 - Failed Dependency
    425 - Too Early
    426 - Upgrade Required
    428 - Preconditon Required
    429 - Too Many Requests 
    431 - Request Header Fiels Too large
    451 - Unavailable for lega reasons

    500 - internal sever error
    501 - Not implemented
    502 - Bad Gateway
    503 - Service Unavailable
    504 - Gateway Timeout
    505 - HTTP Version Not Supproted 
    506 - Variant also negotiates
    507 - insufficient storage
    508 - loop depected
    510 - Not Extnended
    511 - Network Authentication Required 

    Authentification can be:
        import requests
        from requests.auth import HTTPBasicAuth
        
        response = requests.get('https://api.github.com / user, ',
                    auth = HTTPBasicAuth('user', 'pass'))
        
        print(response)

    or you can use a certification file:
        import requests
        
        response = requests.get('https://github.com', verify ='/path/to/certfile')
        
        print(response)
        requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))

    else you can use OAuth1:
        import requests
        from requests_oauthlib import OAuth1

        url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
        auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
        ...               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

        requests.get(url, auth=auth)

    in order to set OAuth2 visit: https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#available-workflows

    Session Objects
    Session object allows one to persist certain parameters across requests. 
    It also persists cookies across all requests made from the Session instance and will use urllib3’s connection pooling. 
    So if several requests are being made to the same host, the underlying TCP connection will be reused, which can result in a significant performance increase. 
    A session object all the methods as of requests.
    the following example show to make cookies:
        import requests

        s = requests.Session()
        
        # make a get request
        s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
        
        r = s.get('https://httpbin.org/cookies')
        
        print(r.text)
        import requests
    
        # create a session object
        s = requests.Session()
        
        # set username and password
        s.auth = ('user', 'pass')
        
        # update headers
        s.headers.update({'x-test': 'true'})
        
        # both 'x-test' and 'x-test2' are sent
        s.get('https://httpbin.org / headers', headers ={'x-test2': 'true'})
        
        # print object
        print(s)
'''
import requests, json
from config import *
import alpaca_trade_api as tradeapi

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')
account = api.get_account()

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)

    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)

    return json.loads(r.content)

