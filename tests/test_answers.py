import unittest
from main import app
from config import UnitTestConfig


class TestForms(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config.from_object(UnitTestConfig)

    def tearDown(self):
        pass

    @staticmethod
    def generate_base_data():
        base_data = {}
        for i in range(1, 26):
            base_data['q' + str(i)] = 'Ja'
        return base_data

    def test_all_yes(self):
        """
        Test special case occurring if all answers are positive
        Note - always recommend module #14
        """
        base_data = self.generate_base_data()

        response = self.client.post('/assessment', data=base_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Redo för lyckad export', str(response.data.decode('utf-8')))

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
        base_data['q2'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Utgångspunkt för lyckad export', str(response.data.decode('utf-8')))

    def test_question_3(self):
        """" Assert module 1 is recommended if bad answer on question 3"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q3'] = 'Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Utgångspunkt för lyckad export', str(response.data.decode('utf-8')))

    def test_question_4(self):
        """" Assert module 1 is recommended if bad answer on question 4"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q4'] = 'Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Utgångspunkt för lyckad export', str(response.data.decode('utf-8')))

    def test_question_5(self):
        """" Assert module 2 is recommended if bad answer on question 5"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q5'] = 'Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Välja exportmarknad', str(response.data.decode('utf-8')))

    def test_question_6(self):
        """" Assert module 2 is recommended if bad answer on question 6"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q6'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Välja exportmarknad', str(response.data.decode('utf-8')))

    def test_question_7(self):
        """" Assert module 3 is recommended if bad answer on question 7"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q7'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Öka hållbarheten', str(response.data.decode('utf-8')))

    def test_question_8(self):
        """" Assert module 3 is recommended if bad answer on question 8"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q8'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Öka hållbarheten', str(response.data.decode('utf-8')))

    def test_question_9(self):
        """" Assert module 4 is recommended if bad answer on question 9"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q9'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Segmentera marknaden', str(response.data.decode('utf-8')))

    def test_question_10(self):
        """" Assert module 5 is recommended if bad answer on question 10"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q10'] = 'Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Segmentera marknaden', str(response.data.decode('utf-8')))

    def test_question_11(self):
        """" Assert module 6 is recommended if bad answer on question 11"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q11'] = 'Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Formulera säljargument', str(response.data.decode('utf-8')))

    def test_question_12(self):
        """" Assert module 6 is recommended if bad answer on question 12"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q12'] = 'Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Formulera säljargument', str(response.data.decode('utf-8')))

    def test_question_13(self):
        """" Assert module 7 is recommended if bad answer on question 13"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q13'] = 'Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Sätta pris', str(response.data.decode('utf-8')))

    def test_question_14(self):
        """" Assert module 7 is recommended if bad answer on question 14"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q14'] = 'Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Analysera konkurrensen', str(response.data.decode('utf-8')))

    def test_question_15(self):
        """" Assert module 8 is recommended if bad answer on question 15"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q15'] = 'Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Välja distributionsstrategi', str(response.data.decode('utf-8')))

    def test_question_16(self):
        """" Assert module 8 is recommended if bad answer on question 16"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q16'] = 'Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Välja distributionsstrategi', str(response.data.decode('utf-8')))

    def test_question_17(self):
        """" Assert module 9 is recommended if bad answer on question 17"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q17'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Hitta samarbetspartners', str(response.data.decode('utf-8')))

    def test_question_18(self):
        """" Assert module 9 is recommended if bad answer on question 18"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q18'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Hitta samarbetspartners', str(response.data.decode('utf-8')))

    def test_question_19(self):
        """" Assert module 10 is recommended if bad answer on question 19"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q19'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Skriva avtal', str(response.data.decode('utf-8')))

    def test_question_20(self):
        """" Assert module 10 is recommended if bad answer on question 20"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q20'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Skriva avtal', str(response.data.decode('utf-8')))

    def test_question_21(self):
        """" Assert module 11 is recommended if bad answer on question 21"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q21'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Planera marknadsföring', str(response.data.decode('utf-8')))

    def test_question_22(self):
        """" Assert module 12 is recommended if bad answer on question 22"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q22'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Göra etableringskalkyl', str(response.data.decode('utf-8')))

    def test_question_23(self):
        """" Assert module 12 is recommended if bad answer on question 23"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q23'] = 'Delvis'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Göra etableringskalkyl', str(response.data.decode('utf-8')))

    def test_question_24(self):
        """" Assert module 13 is recommended if bad answer on question 24"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q24'] = 'Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('exportvillkor', str(response.data.decode('utf-8')))

    def test_question_25(self):
        """" Assert module 13 is recommended if bad answer on question 25"""
        base_data = self.generate_base_data()

        # Substitute answers to meet test criteria
        base_data['q25'] = 'Nej'

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('exportvillkor', str(response.data.decode('utf-8')))

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

    def test_error(self):
        """Assert error message is shown if one question is left unanswered"""
        base_data = self.generate_base_data()

        base_data['q5'] = None

        response = self.client.post('/assessment', data=base_data)
        self.assertIn('Oops', str(response.data.decode('utf-8')))


if __name__ == '__main__':
    unittest.main()
