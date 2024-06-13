import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBneuLuefXVPM3_jYPIE3aw564qOnYnBjk"
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)
request = youtube.commentThreads().list(
    part="snippet",
    videoId="dEU2ibHQnjM",
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

df = pd.DataFrame(comments, columns = ['auother', 'like', 'textDisplay'])
print(df)
