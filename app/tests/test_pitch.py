import unittest
from app.models import Pitch

id = db.Column(db.Integer, primary_key=True)
    pitch_title = db.Column(db.String)
    pitch_body = db.Column(db.String)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category = db.Column(db.String(255))
    pitch = db.relationship("Comment", backref="user_pitch", lazy="dynamic")

class TestUser(unittest):
    def setUp(self):
        self.new_pitch = Pitch(pitch_title='Graphic Designer', pitch_body="Hi, I'm Molly, so nice to meet you!...", posted_at="2019-05-27 14:15:43.587649", id=1, category="Elevator")

    def tearDown(self):
        User.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title, 'Graphic Designer')
        self.assertEquals(self.new_pitch.body, 'Hi, I\'m Molly, so nice to meet you!...')
        self.assertEquals(self.new_pitch.posted_at, '2019-05-27 14:15:43.587649')
        self.assertEquals(self.new_pitch.id, '1')
        self.assertEquals(self.new_category, 'Elevator')
    

if __name__ == "__main__":
    unittest.main()