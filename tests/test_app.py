from src.models import PreRating, WatchVideo, PostRating


def test_pre_rating_page(client):
    """ Test the response of the Pre Rating page """
    response = client.get("/pre-rating")
    assert b"<title>Pre Rating</title>" in response.data
    
def test_pre_rating_form(client, app):
    """ Tests the Pre rating form functionality """
    
    data = dict(rating=4)
    client.post("/pre-rating", data=data)
    
    with app.app_context():
       last_row = PreRating.query.order_by(PreRating.id.desc()).first()
       assert last_row.rating == 4
    
    
def test_video_page(client):
    """ Test the response of the Video page """
    response = client.get("/video-instructions")
    assert b"<title>Video Instructions</title>" in response.data
    
def test_video_form(client, app):
    """ Tests the HTML Video Watch functionality """
    client.post("/video-instructions", data="")
    
    with app.app_context():
       row = WatchVideo.query.filter(WatchVideo.id==1).first()
       assert row.times_watched == 1
    
    
def test_post_rating_page(client):
    """ Test the response of the Post Rating page """
    response = client.get("/post-rating")
    assert b"<title>Post Rating</title>" in response.data
    
def test_post_rating_form(client, app):
    """ Tests the Post rating form functionality """
    data = dict(rating=1)
    client.post("/post-rating", data=data)
    
    with app.app_context():
       last_row = PostRating.query.order_by(PostRating.id.desc()).first()
       assert last_row.rating == 1