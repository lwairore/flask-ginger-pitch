import unittest
from app.models import User

class TestUser(unittest):
    def setUp(self):
        self.user_John = User(username='John', password="angel", email="john@gmail.com", id=1, bio="Iam a junior developer", profile_pic_path="app/static/photos")

    def tearDown(self):
        User.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_John.id, 1)
        self.assertEquals(self.new_John.username. 'John')
        self.assertEquals(self.new_John.title, 'Awesome')
        self.assertEquals(self.new_John.bio, '"Iam a junior developer')
        self.assertEquals(self.new_John.postedAt, '2019-05-27 14:15:43.587649')
        self.assertEquals(self.new_John.email, 'john@gmail.com')
        self.assertEquals(self.new_John.profile_pic_path, 'app/static/photos')



    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('angel'))

if __name__ == "__main__":
    unittest.main()
