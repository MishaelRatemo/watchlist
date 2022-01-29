import  unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Review class
    '''    
    def  setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_review = Review(2020,'Adu','hdjkshjdhkhdjkdhk.jpg','The truth on the ground')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_review, Review))