from cgi import parse_qs
from newtemplate import html
def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    plus = -1
    multiple = -1
    try:
        a,b = int(a),int(b)
        plus = a + b
        multiple = a * b
    except ValueError:
        plus = -1
        multiple = -1  
    response_body = html % {'sum':plus, 'prod':multiple}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
