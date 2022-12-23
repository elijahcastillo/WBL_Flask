from src import db


class PreRating(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rating = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"Pre('{self.id}'), '{self.rating}'"
    
class PostRating(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rating = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"Post('{self.id}'), '{self.rating}'"
    
class WatchVideo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    times_watched = db.Column(db.Integer, nullable=False, default=1)
    
    def __repr__(self):
        return f"Watched('{self.id}'), '{self.times_watched}'"
