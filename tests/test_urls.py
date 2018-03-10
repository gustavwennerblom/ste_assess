import unittest
from main import app
from config import UnitTestConfig

class TestUrls(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config.from_object(UnitTestConfig)

    def tearDown(self):
        pass

    def test_root(self):
        """
        Test redirect on root
        """
        response = self.client.get('/')
        status_code = response.status_code
        self.assertEqual(status_code, 302)

    def test_home(self):
        """
        Test validity of assessment page
        """
        response = self.client.get('/assessment')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Kort instruktionstext här', str(response.data.decode('utf-8')))

    def test_error_500(self):
        """
        NOT WORKING - CANNOT REPLICATE FAILURE DUE TO CUSTOM ERROR HANDLING
        Assert Internal Server Error (500) triggers custom page        
        """
        pass
        # response = self.client.post('/assessment', foo="bar")
        # self.assertEqual(response.status_code, 200)
        # self.assertIn('Whoops', str(response.data.decode('utf-8')))

class TestForms(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config.from_object(UnitTestConfig)

    def tearDown(self):
        pass

    def test_submit_assessment(self):
        """
        Test form can be submitted
        """
        base_data = {}
        for i in range(1,26):
            base_data['q' + str(i)] = 'Ja'

        response = self.client.post('/assessment', data=base_data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
