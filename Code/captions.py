# import pandas as pd
# from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

# def get_captions(video_id):
    
#     ## Handeling the error
#     try:
#         transcript = YouTubeTranscriptApi.get_transcript(video_id)
#         caption_text = " ".join([entry['text'] for entry in transcript])
#         return True, caption_text
#     except TranscriptsDisabled:
#         return False, "No captions Availble  :()"
#     except NoTranscriptFound:
#         return False, "No transcript availablr :()"

# def main():
#     df = pd.read_csv(r'Movies.csv')
#     captions_data = []

#     for index, row in df.iterrows():
#         video_id = row['Video URL'].split('v=')[-1]  
#         captions_available, caption_text = get_captions(video_id)
#         captions_data.append({
#             'Video URL': row['Video URL'],
#             'Title': row['Title'],
#             'Captions Available': 'Yes' if captions_available else 'No',
#             'Caption Text': caption_text
#         })

#     captions_df = pd.DataFrame(captions_data)

#     captions_df.to_csv('Movies_captions.csv', index=False)
#     print("Captions data saved to Science.csv")

# if __name__ == "__main__":
#     main()

import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import logging

# Configure logging
logging.basicConfig(
    filename="youtube_captions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_captions(video_id):
    """
    Fetch captions for a given video ID using YouTubeTranscriptApi.
    Returns a tuple indicating if captions are available and the text or error message.
    """
    try:
        logging.info(f"Fetching captions for video ID: {video_id}")
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        caption_text = " ".join([entry['text'] for entry in transcript])
        return True, caption_text
    except TranscriptsDisabled:
        logging.warning(f"Captions disabled for video ID: {video_id}")
        return False, "No captions available :()"
    except NoTranscriptFound:
        logging.warning(f"No transcript found for video ID: {video_id}")
        return False, "No transcript available :()"
    except Exception as e:
        logging.error(f"Unexpected error while fetching captions for video ID {video_id}: {e}")
        return False, f"Error fetching captions: {e}"

def main():
    """
    Reads video data from a CSV file, fetches captions for each video, 
    and saves the captions data to a new CSV file.
    """
    try:
        logging.info("Starting the captions extraction process.")
        input_file = 'Movies.csv'
        output_file = 'Movies_captions.csv'

        df = pd.read_csv(input_file)
        logging.info(f"Loaded {len(df)} videos from {input_file}.")

        captions_data = []

        for index, row in df.iterrows():
            video_url = row['Video URL']
            video_id = video_url.split('v=')[-1]  
            logging.info(f"Processing video {index + 1}/{len(df)}: {video_url}")

            captions_available, caption_text = get_captions(video_id)
            captions_data.append({
                'Video URL': video_url,
                'Title': row['Title'],
                'Captions Available': 'Yes' if captions_available else 'No',
                'Caption Text': caption_text
            })

        captions_df = pd.DataFrame(captions_data)
        captions_df.to_csv(output_file, index=False)

        logging.info(f"Captions data saved to {output_file}")
        print(f"Captions data saved to {output_file}")
        
    except FileNotFoundError as e:
        logging.error(f"Input file not found: {e}")
        print("Error: Input file not found. Please ensure 'Movies.csv' exists.")
        
    except Exception as e:
        logging.exception("An unexpected error occurred during the script execution.")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
