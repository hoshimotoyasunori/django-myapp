from django.test import TestCase
import datetime
from .models import Diary

# Create your tests here.

class DiaryModelTests(TestCase):

    def test_diary_has_date(self):
        """
        作成した日記データに日付が付与されているか確認
        """
        Diary.objects.create(title='test_title', text='test_text')
        actual_diary = Diary.objects.get(title='test_title')
        self.assertIsInstance(actual_diary.date, datetime.date)
    
    def test_save_and_retrieve(self):
        """
        日記データの保存と取得を確認
        """
        Diary.objects.create(title='test_title', text='test_text')
        actual_diary = Diary.objects.get(title='test_title')
        self.assertEqual(actual_diary.title, 'test_title')