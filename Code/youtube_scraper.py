import requests
import pandas as pd
from dotenv import load_dotenv
import os
import logging

# Logging for tracking 
logging.basicConfig(
    filename="youtube_scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fetch_top_videos_paginated(API_KEY, genre, max_results=500):
    logging.info(f"Fetching top videos for genre ID: {genre}")
    videos = []
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&type=video&videoCategoryId={genre}&key={API_KEY}"
    next_page_token = None

    '''
    The YouTube Data API's search endpoint has a hard limit of 50 results per request
    
    so handdling the 500 Video request with a Paginating using {next_page_token} in Youtube Apis
    
    '''

    while len(videos) < max_results:
        if next_page_token:
            url += f"&pageToken={next_page_token}"

        response = requests.get(url)
        if response.status_code != 200:
            logging.error(f"Error fetching videos: {response.status_code}, {response.text}")
            break

        data = response.json()
        videos.extend(data.get('items', []))

        logging.info(f"Fetched {len(videos)} videos so far.")
        next_page_token = data.get('nextPageToken')
        if not next_page_token:
            logging.info("No more pages available.")
            break

    logging.info(f"Total videos fetched: {len(videos)}")
    return videos[:max_results]  


def extract_video_details(API_KEY, video_id):
    logging.info(f"Fetching details for video ID: {video_id}")
    
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id={video_id}&key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        
        logging.error(f"Error fetching video details for {video_id}: {response.status_code}, {response.text}")
        return {}
    
    return response.json()


def main(API_KEY, genre):
    logging.info("Starting script...")
    
    try:
        video_data = fetch_top_videos_paginated(API_KEY, genre)

        videos = []
        for item in video_data:
            video_id = item['id']['videoId']
            details = extract_video_details(API_KEY, video_id)

            if details.get('items'):
                video_info = details['items'][0]
                video_details = {
                    'Video URL': f"https://www.youtube.com/watch?v={video_id}",
                    'Title': video_info['snippet']['title'],
                    'Description': video_info['snippet']['description'],
                    'Channel Title': video_info['snippet']['channelTitle'],
                    'Keyword Tags': ', '.join(video_info['snippet'].get('tags', [])),
                    'YouTube Video Category': video_info['snippet']['categoryId'],
                    'Topic Details': '',
                    'Video Published at': video_info['snippet']['publishedAt'],
                    'Video Duration': video_info['contentDetails']['duration'],
                    'View Count': video_info['statistics'].get('viewCount', 0),
                    'Comment Count': video_info['statistics'].get('commentCount', 0),
                    'Captions Available': 'true' if 'caption' in video_info['contentDetails'] else 'false',
                    'Caption Text': '',
                    'Location of Recording': video_info['snippet'].get('location', '')
                }
                videos.append(video_details)
                logging.info(f"Processed video ID: {video_id}")

        df = pd.DataFrame(videos)
        output_file = 'Movies.csv'
        df.to_csv(output_file, index=False)
        logging.info(f"Data saved to {output_file}")
        print("Data saved successfully.")
        
        
    except Exception as e:
        logging.exception("Error occurred script execution.")
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    load_dotenv()  
    API_KEY = os.getenv('API_KEY')
    
    if not API_KEY:
        logging.error("API_KEY is missing.")
        print("Error: API_KEY is missing.")
        
    else:
        genre = input("Enter the genre ID: ") 
        main(API_KEY, genre)
