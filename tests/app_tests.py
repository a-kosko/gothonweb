from nose.tools import *
from gothonweb import app

app.app.config['TESTING'] = True
web = app.app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/hello', follow_redirects=True)
    print(">>> web", )
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill Out This Form", rv.data)

    data = {'name': 'Vlad', 'greet': 'Hola'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert_in(b"Vlad", rv.data)
    assert_in(b"Hola", rv.data)
