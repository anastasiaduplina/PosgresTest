import pytest

from flaskr.app import app

# def test_index_route():
#     client = app.test_client()
#     url = '/'
#     response = client.get(url)
#     #assert response.get_data() == b'Hello World!'
#     assert response.status_code == 302
def test_login():
    client = app.test_client()

    response =client.post('/login', data=dict(
        check='on',
        username='qwerty',
        password='123'
        ), follow_redirects=True)

    #assert b'Hello' in response.get_data()

# def test_registration():
#     client=app.test_client()
#     response=client.post('/register',data=dict(
#         check='',
#         username='hgjfjyn',
#         password='123'
#     ), follow_redirects=True)
#     assert b'Hello' in response.get_data()
def transaction():
    client = app.test_client()
    # i = 1
    # while i < 10:
    response = client.post('/transactions', data=dict(
        to='user',
        amount='1',
        comment='comment'
        ), follow_redirects=True)
        # i += 1
    #assert b'Hello,' in response.get_data()
# def test_logout():
#     client = app.test_client()
#     client.post('/login', data=dict(
#         check='on',
#         username='qwerty',
#         password='123'
#     ), follow_redirects=True)
#     response = client.post('/logout', follow_redirects=True)
#     #assert b'login' in response.get_data()
#     #assert response.status_code == 200



