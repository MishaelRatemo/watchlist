import  unittest
from app.models import Review
# we need to import the SQLAlchemy database instance and User class for testing
from app.models import User 
from app import db

class ReviewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Review class
    '''    
    def  setUp(self):
        '''
        Set up method that will run before every Test
        '''
       
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_review = Review(movie_id=12345,movie_title='Review for movies',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='This movie is the best thing since sliced bread',user = self.user_James )
      
    def tearDown(self):
        Review.query.delete()
        User.query.delete()
        
    #  check if the values of variables are correctly being placed.
    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.movie_id,12345)
        self.assertEquals(self.new_review.movie_title,'Review for movies')
        self.assertEquals(self.new_review.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_review.movie_review,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_review.user,self.user_James)
     
    #We then create a test for our save review method. We also query the database to confirm that we actually have data saved.   
    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all())>0)
        
    def test_get_review_by_id(self):
    
        self.new_review.save_review()
        got_reviews = Review.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_review, Review))