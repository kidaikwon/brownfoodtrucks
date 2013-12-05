from flask import render_template
from app import app
import mytweets

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/<username>/tweets')
def user_tweets(username):
    usertweets, posttweets= mytweets.get_tweets(username);
    user= {'nickname': username}
    posts= [
    {
        'author': {'nickname': username},
        'body': posttweets[0]   
    },
    {
        'author': {'nickname': username},
        'body': posttweets[1]   
    },
    {
        'author': {'nickname': username},
        'body': posttweets[2]   
    }
    ]
    return render_template("base.html",
        title = 'Home',
        user = user,
        posts = posts)
