def simpleapp(environ, start_response):
    key = 'QUERY_STRING'
    if key in environ:
        query = environ[key]
    else:
        query = ''
    querylist = query.split('&')
    strout = "\n".join(querylist)
    start_response("200 OK", [("Content-Type", "text/plain")])
    return iter([strout.encode('utf-8')])