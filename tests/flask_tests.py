# -*- coding: utf-8 -*-
"""
    tests.flask_tests
    ~~~~~~~~~~~~~~~~~~~~~~~
    Tests the Flask-based backend
"""
from app import app
import unittest
import flask

class FlaskTests(unittest.TestCase): 
    def setUp(self):
    	"""
		Initialize flask environment
        """
        self.app = app.test_client()
        self.app.testing = True 

    def test_triangle_func(self):
    	"""
        Ensures the Triangle: (0,0) (1,0) (0,1) contains the origin 
        """
        response = self.app.post('/api/containsOrigin', data=dict(vertices = '0,0,1,0,0,1'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 'true\n')


    def test_triangle_func(self):
    	"""
        Ensures that the api sends a 400 response when an invalid triangle is provided
        """
        response = self.app.post('/api/containsOrigin', data=dict(vertices = '0,0,1,0,0'))
        self.assertEqual(response.status_code, 400) 

if __name__ == '__main__':
	unittest.main()