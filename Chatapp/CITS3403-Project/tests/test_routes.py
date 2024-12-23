import sys
import os
sys.path.append(os.path.abspath('..'))
import unittest
import json
from run import app

#undo data base first



class TestController(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_direct_jump_to_chat(self):
        response = self.app.get('/chat')
        self.assertEqual(response.status_code, 302) # without validation, it will be jump back to /login

    def test_direct_jump_to_search(self):
        response = self.app.get('/search')
        self.assertEqual(response.status_code, 302) # without validation, it will be jump back to /login

    def test_post_request_login_right(self):
        response = self.app.post('/login', data={'username': 'AH', 'password': '1207'})
        self.assertEqual(response.status_code, 200) # get a response
        self.assertIn(b'success', response.data)

    def test_post_request_login_wrong(self):
        response = self.app.post('/login', data={'username': 'AH', 'password': '0000'})
        self.assertEqual(response.status_code, 200) # get a response
        self.assertIn(b'invalid', response.data)

    def test_post_request_register_right(self):           # test once and need to reset db
        response = self.app.post('/register', data={'username': 'test1', 'password': '1'})
        self.assertEqual(response.status_code, 200) # get a response
        self.assertIn(b'success', response.data)

    def test_post_request_register_wrong(self):
        response = self.app.post('/register', data={'username': 'AH', 'password': '1207'})
        self.assertEqual(response.status_code, 200) # get a response
        self.assertIn(b'exist', response.data)

    def test_logout(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302) # logout success and redirected


class TestChat(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_chat_function(self):
        response = self.app.post('/login', data={'username': 'AH', 'password': '1207'})  #first we get validation
        self.assertEqual(response.status_code, 200) # get a response
        self.assertIn(b'success', response.data)
        headers = {'Content-Type': 'application/json'}
        data = {'message': 'This is a test, please reply with unittest'}
        json_data = json.dumps(data, default=str)
        response = self.app.post('/chat', headers=headers, data=json_data) #talk to chatbot
        self.assertEqual(response.status_code, 200) # get a response
        self.assertIn(b'unittest', response.data)
    
    def test_search_function(self):
        response = self.app.post('/login', data={'username': 'AH', 'password': '1207'})  #first we get validation
        self.assertEqual(response.status_code, 200) # get a response
        self.assertIn(b'success', response.data)
        headers = {'Content-Type': 'application/json'}
        data = {'query': 'unittest'}
        json_data = json.dumps(data, default=str)
        response = self.app.post('/search', headers=headers, data=json_data) # asking for history
        self.assertEqual(response.status_code, 200) # get a response
        self.assertIn(b'unittest', response.data)
