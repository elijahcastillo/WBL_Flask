from flask import Blueprint, render_template, flash, redirect, url_for, request
from src.forms import RatingForm
from src.models import PreRating, WatchVideo, PostRating
from src import db


routes = Blueprint("routes", __name__, template_folder="/")



@routes.route("/", methods=["POST", "GET"])
@routes.route("/pre-rating", methods=["POST", "GET"])
def preRating():
    form = RatingForm()
    if form.validate_on_submit():
        #add rating to db
        rating = int(form.rating.data)
        pre_rating = PreRating(rating=rating)
        db.session.add(pre_rating)
        db.session.commit()
        
        #redirect user to next page
        flash(f"Pre Stress level recorded as {rating}", "success")
        return redirect(url_for("routes.videoInstructions"))
        
    
    return render_template("preRating.html", form=form)

@routes.route("/video-instructions", methods=["POST", "GET"])
def videoInstructions():
    if(request.method == "POST"):
        #check if row has been created
        row = db.session.query(WatchVideo).filter(WatchVideo.id==1).first()
        if not row :
            #Create new row
            watch_counter = WatchVideo()
            db.session.add(watch_counter)
            db.session.commit()
        else:
            #Increment watch count
            row.times_watched = row.times_watched + 1
            db.session.commit()
        flash(f"Excercise Compleated", "success")
    return render_template("videoInstructions.html")



@routes.route("/post-rating", methods=["POST", "GET"])
def postRating():
    form = RatingForm()
    if form.validate_on_submit():
        #add rating to db
        rating = int(form.rating.data)
        post_rating = PostRating(rating=rating)
        db.session.add(post_rating)
        db.session.commit()
        
        flash(f"Post Stress level recorded as {form.rating.data}", "success")
        
    return render_template("postRating.html", form=form)