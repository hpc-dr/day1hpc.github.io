# API client library
import googleapiclient.discovery
import json

# API information
api_service_name = "youtube"
api_version = "v3"
# API key
DEVELOPER_KEY = "AIzaSyBvcdVuPQ1bZoTxA2mzMY7PUz2OJNNqB6g"
# API client
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)
# 'request' variable is the only thing you must change
# depending on the resource and method you need to use
# in your query
# request = youtube.search().list(
#     part="id"
# )

request = youtube.channels().list(
    part="snippet,contentDetails,statistics,topicDetails",
    id="UChSIn5kcWQvJxW17KIjdLVw"
)
# Query execution
response = request.execute()
# Print the results
# print(json.dumps(response, indent=4))

# uploads playlist
UPLOADS_PLAYLIST_ID = "UUhSIn5kcWQvJxW17KIjdLVw"

request = youtube.playlistItems().list(
    part="snippet,contentDetails",
    playlistId=UPLOADS_PLAYLIST_ID,
    maxResults=2
)
# Query execution
response = request.execute()
# Print the results
# print(json.dumps(response, indent=4))

video_ids = []
for i in response['items']:
    print(i['contentDetails']['videoId'])
    video_ids.append(i['contentDetails']['videoId'])


request = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    id=",".join(video_ids)
)
response = request.execute()
print(json.dumps(response, indent=4))

# RSS
# https://www.youtube.com/feeds/videos.xml?channel_id=UChSIn5kcWQvJxW17KIjdLVw
