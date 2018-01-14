import unittest
from main import app
from config import UnitTestConfig

class TestForms(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config.from_object(UnitTestConfig)

    def tearDown(self):
        pass

    def generate_base_data(self):
        base_data = {}
        for i in range(1, 26):
            base_data['q' + str(i)] = 'Ja'
        return base_data

    def test_all_yes(self):
        """
        Test special case occurring if all answers are positive
        """
        base_data = self.generate_base_data()

        response = self.client.post('/assessment', data=base_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Exportmästare!', str(response.data.decode('utf-8')))

    def test_question_1(self):
        """" Assert module 1 is recommended if bad answer on question 1"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q1'] = 'Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Utgångspunkt för lyckad export', str(response.data.decode('utf-8')))

    def test_question_2(self):
        """" Assert module 1 is recommended if bad answer on question 2"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q2']='Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Utgångspunkt för lyckad export', str(response.data.decode('utf-8')))

    def test_question_3(self):
        """" Assert module 1 is recommended if bad answer on question 3"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q3']='Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Utgångspunkt för lyckad export', str(response.data.decode('utf-8')))

    def test_question_4(self):
        """" Assert module 1 is recommended if bad answer on question 4"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q4']='Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Utgångspunkt för lyckad export', str(response.data.decode('utf-8')))

    def test_question_5(self):
        """" Assert module 2 is recommended if bad answer on question 5"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q5']='Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Välja exportmarknad', str(response.data.decode('utf-8')))

    def test_recommend_module_2(self):
        """" Assert module 2 is recommended if bad answer on question 5 or 6"""
        # Build base set of "yes" answers
        base_data = {}
        for i in range(1, 26):
            base_data['q' + str(i)] = 'Ja'

        # Substitute answers to meet test criteria
        base_data['q5'] = 'Nej'
        base_data['q6'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Välja exportmarknad', str(response.data.decode('utf-8')))

    def test_recommend_module_3(self):
        """" Assert module 3 is recommended if bad answer on question 7 or 8"""
        # Build base set of "yes" answers
        base_data = {}
        for i in range(1, 26):
            base_data['q' + str(i)] = 'Ja'

        # Substitute answers to meet test criteria
        base_data['q7'] = 'Nej'
        base_data['q8'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Öka hållbarheten', str(response.data.decode('utf-8')))

    def test_recommend_module_4(self):
        """" Assert module 4 is recommended if bad answer on question 9 or 10"""
        # Build base set of "yes" answers
        base_data = {}
        for i in range(1, 26):
            base_data['q' + str(i)] = 'Ja'

        # Substitute answers to meet test criteria
        base_data['q9'] = 'Nej'
        base_data['q10'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Segmentera marknaden', str(response.data.decode('utf-8')))

    def test_recommend_module_5(self):
        """" Assert module 5 is recommended if bad answer on question 11 or 12"""
        # Build base set of "yes" answers
        base_data = {}
        for i in range(1, 26):
            base_data['q' + str(i)] = 'Ja'

        # Substitute answers to meet test criteria
        base_data['q11'] = 'Nej'
        base_data['q12'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Formulera säljargument', str(response.data.decode('utf-8')))


if __name__ == '__main__':
    unittest.main()
