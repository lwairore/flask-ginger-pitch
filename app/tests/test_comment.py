import unittest
from app.models import User, Comment
from flask_login import current_user
from app import db

class TestComments(unittest.TestCase):
    def setUp(self):        
        self.new_comment = Comment(pitch_id=12, title='Awesome', comment="Nice presentation...", postedAt="2019-05-27 14:15:43.587649", user_id=1)

    def tearDown(self):
        Comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_id, 12)
        self.assertEquals(self.new_comment.title, 'Awesome')
        self.assertEquals(self.new_comment.comment, 'Nice presentation...')
        self.assertEquals(self.new_comment.postedAt, '2019-05-27 14:15:43.587649')
        