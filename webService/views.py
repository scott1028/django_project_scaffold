# coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponse


# api: PATCH http://127.0.0.1:3333/api/test_multipart_patch/ by multipart format
# test multipart patch
def test_multipart_patch(request):
    import cgi
    from io import BytesIO
    print request.body
    print '='*40
    ctype, pdict = cgi.parse_header(request.META['CONTENT_TYPE'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(BytesIO(request.body), pdict)
        print postvars
    resp = HttpResponse(status=201)
    resp['Content-Type'] = 'application/json'
    return resp
