from dotenv import load_dotenv
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
import os
import mysql.connector
from flask import Flask,jsonify

app = Flask(__name__)



# Load environment variables from .env file
load_dotenv('.env')

# Get API key from environment variables
API_KEY = os.getenv('API_KEY')
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='Kunals#2004',
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
            maxResults=100
        )
        response = request.execute()

        
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            name = comment['authorDisplayName'],
            like = comment['likeCount'],
            text = comment['textDisplay']
            comments.append([
                name,
                like,
                text
            ])
            
        return comments

    except googleapiclient.errors.HttpError as error:
        print(f'An error occurred: {error}')
        return []
    
@app.route("/comment", methods=['GET'])
def get_comments():
    video_id = 'dEU2ibHQnjM'
    if not video_id:
        return jsonify({"error": "video_id is required"}), 400  
    comments = get_youtube_comments(video_id)
    df = pd.DataFrame(comments, columns=['author', 'like', 'textDisplay'])
    print(df)
    return jsonify(comments)

# Example usage
if __name__ == '__main__':
    # VIDEO_ID = 'dEU2ibHQnjM'
    # comments = get_youtube_comments(VIDEO_ID)

    # Convert to DataFrame and print
    # df = pd.DataFrame(comments, columns=['author', 'like', 'textDisplay'])
    # print(df)

    app.run(debug=True)
