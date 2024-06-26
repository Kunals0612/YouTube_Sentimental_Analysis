from dotenv import load_dotenv
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
import os
import mysql.connector
from flask import Flask,jsonify,request

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv('.env')

# Get API key from environment variables
API_KEY = os.getenv('API_KEY')
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='youtube'
# )
# print(mydb)

# if mydb.is_connected():
#     print("DATABASE is connected")

if not API_KEY:
    raise ValueError("No API key found. Please set your API key in the .env file.")

# Set up YouTube API client 
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=API_KEY)

# Function to get YouTube comments
comments = []
def get_youtube_comments(video_id):
    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=30000
        )
        response = request.execute()

        
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            name = comment['authorDisplayName'],
            like = comment['likeCount'],
            text = comment['textDisplay']
            published_at = comment['publishedAt']
            published_at = published_at[:10]
            comments.append([
                name,
                like,
                text,
                published_at
            ])
            
        return comments

    except googleapiclient.errors.HttpError as error:
        print(f'An error occurred: {error}')
        return []
@app.route("/process", methods=['POST'])
def process_text():
    if request.content_type != 'text/plain':
        return jsonify({"error": "Content-Type must be text/plain"}), 400

    text = request.data.decode('utf-8')
    # Here you can process the text as needed
    # For demonstration, let's just return the text in uppercase
    processed_text = text.upper()

    return jsonify({"processed_text": processed_text})
@app.route("/comment", methods=['POST'])
def get_comments():
    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 400 
    data = request.get_json()
    video_id = data.get('video_id')
    if not video_id:
        return jsonify({"error": "video_id is required"}), 400
    comments = get_youtube_comments(video_id)
    return jsonify({"comments": comments})

# Example usage
if __name__ == '__main__':
    # VIDEO_ID = 'dEU2ibHQnjM'
    # comments = get_youtube_comments(VIDEO_ID)

    # Convert to DataFrame and print
    # df = pd.DataFrame(comments, columns=['author', 'like', 'textDisplay'])
    # print(df)

    app.run(debug=True)
