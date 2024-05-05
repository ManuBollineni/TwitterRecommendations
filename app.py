from flask import Flask, session, redirect, url_for, request, render_template, flash
import re
import random
from neo4j import GraphDatabase
from flask_session import Session  # This is an extension to provide sessions

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'  # Make sure this is correctly set

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "neo4jneo4j"))
Session(app)

# Create Tweet Node
def create_tweet(tx, tweet_text, tweet_id):
    query = """
    CREATE (t:Tweet {
        text: $text,
        createdAt: datetime(),
        id: $id
    })
    RETURN t
    """
    result = tx.run(query, text=tweet_text, id=tweet_id)
    print(tweet_text)
    return result.single()[0]

def add_tweet_to_db(tweet_text, tweet_id):
    with driver.session() as session:
        tweet = session.execute_write(create_tweet, tweet_text, tweet_id)
        print(f"Tweet created: ")

@app.route('/')
def index():
    tweets = session.pop('tweets', None)  # Retrieve and remove tweets from session
    if not tweets:
        tweets = [{'content': 'No tweets available.', 'createdAt': 'N/A'}]
    return render_template('index.html', tweets=tweets)
# def get_recent_tweets(limit=10):
#     with driver.session() as session:
#         result = session.run("""
#             MATCH (n:Tweet)
#             RETURN n.text AS content, n.created_at AS createdAt
#             LIMIT $limit
#         """, limit=limit)
#         return [{'content': record['content'], 'createdAt': record['createdAt'].isoformat() if record['createdAt'] else 'Unknown time'} for record in result]


@app.route('/submit_tweet', methods=['GET', 'POST'])
def submit_tweet():
    if request.method == 'POST':
        tweet_content = request.form['tweet_content']
        hashtags = extract_hashtags(tweet_content)
        add_tweet_to_db(tweet_content, random.randint(1, 1000000))
        recommended_tweets = get_recommended_tweets(hashtags)
        session['tweets'] = recommended_tweets  # Store tweets in session
        return redirect(url_for('index'))  # Redirect to the index
    return render_template('index.html')

def get_recommended_tweets(hashtags=["umbc", "school"]):
    print(hashtags)
    with driver.session() as session:
        result = session.run("""
            MATCH (t:Tweet)
            WHERE ANY(tag IN $hashtags WHERE t.text CONTAINS tag)
            RETURN t.text AS content, t.createdAt AS createdAt
            LIMIT 10

        """, hashtags=hashtags)
        return [{'content': record['content'], 'createdAt': record['createdAt']} for record in result]

# Return Hashtags from Tweet
def extract_hashtags(text):
    # This regex finds all words that start with '#'
    hashtags = re.findall(r'#\w+', text)
    return hashtags
if __name__ == '__main__':
    app.run(debug=True, port=5006)