from django.test import TestCase
from django.urls import reverse

class CalcTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'calc/index.html')

    def test_calculate_addition(self):
        response = self.client.post(reverse('calculate'), {'num1': '10', 'num2': '5', 'operation': 'add'})
        self.assertEqual(response.context['result'], 15)

    def test_calculate_substraction(self):
        response = self.client.post(reverse('calculate'), {'num1': '10', 'num2': '5', 'operation': 'substract'})
        self.assertEqual(response.context['result'], 5)

    def test_calculate_multiplication(self):
        response = self.client.post(reverse('calculate'), {'num1': '10', 'num2': '5', 'operation': 'multiply'})
        self.assertEqual(response.context['result'], 50)

    def test_calculate_division(self):
        response = self.client.post(reverse('calculate'), {'num1': '10', 'num2': '5', 'operation': 'divide'})
        self.assertEqual(response.context['result'], 2)
    def test_calculate_division_by_zero(self):
        response = self.client.post(reverse('calculate'), {'num1': '10', 'num2': '0', 'operation': 'divide'})
        self.assertEqual(response.context['result'], 'Error! Division by zero')

    def test_invalid_operation(self):
        response = self.client.post(reverse('calculate'), {'num1': '10', 'num2': '5', 'operation': 'invalid'})
        self.assertEqual(response.context['result'], 'Invalid operation')
