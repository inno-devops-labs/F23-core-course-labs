"""Module for test siutes"""
from datetime import datetime, timezone, timedelta
from django.test import TestCase, Client
from django.urls import reverse


class CurrentTimeTestCase(TestCase):
    """Class Spec for tests """

    def setUp(self):
        self.client = Client()

    def test_current_time(self):
        """current time should work correctly"""

        url = reverse('current_time')
        response = self.client.get(url)
        moscow_tz = timezone(timedelta(hours=3))
        now = datetime.now(moscow_tz)
        expected = now.strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(response.content.decode(), expected)
