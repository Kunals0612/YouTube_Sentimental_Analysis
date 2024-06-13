from dotenv import load_dotenv
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
import os

# Load environment variables from .env file
load_dotenv('.env')

# Get API key from environment variables
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError("No API key found. Please set your API key in the .env file.")

# Set up YouTube API client
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=API_KEY)

# Function to get YouTube comments
def get_youtube_comments(video_id):
    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100
        )
        response = request.execute()

        comments = []
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append([
                comment['authorDisplayName'],
                comment['likeCount'],
                comment['textDisplay']
            ])

        return comments

    except googleapiclient.errors.HttpError as error:
        print(f'An error occurred: {error}')
        return []

# Example usage
if __name__ == '__main__':
    VIDEO_ID = 'dEU2ibHQnjM'
    comments = get_youtube_comments(VIDEO_ID)

    # Convert to DataFrame and print
    df = pd.DataFrame(comments, columns=['author', 'like', 'textDisplay'])
    print(df)
