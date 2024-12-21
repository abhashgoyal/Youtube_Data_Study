# YouTube Captions and Video Scraper

A sophisticated system that fetches YouTube video captions and details by utilizing the YouTube Data API and the YouTube Transcript API. This project integrates data from YouTube to provide comprehensive insights into video content and availability of captions.

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="shields">
<img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="shields">
<img src="https://img.shields.io/badge/requests-FF6F61?style=for-the-badge&logo=requests&logoColor=white" alt="shields">
<img src="https://img.shields.io/badge/youtube--transcript--api-FF4500?style=for-the-badge&logo=youtube&logoColor=white" alt="shields">
</p>

## 🧐 Features

Here are some of the project's best features:

* **Captions Fetching**: Retrieves captions for YouTube videos using the YouTube Transcript API.
* **Video Details Scraping**: Collects detailed information about videos, including titles, descriptions, and statistics.
* **Multi-source Data Integration**: Combines data from YouTube's search and video details endpoints.
* **Error Handling**: Robust error management for API calls and data processing.
* **Logging**: Comprehensive logging for tracking the execution flow and errors.

## 💻 Built with

Technologies used in the project:

* Python: Core programming language
* pandas: Data manipulation
* requests: HTTP requests for API calls
* youtube-transcript-api: Fetching video transcripts
* dotenv: Managing environment variables

## ⚙️ Usage

### YouTube Scraper Script

1. **Initialization**: 
   - The script fetches top videos based on a specified genre ID using the YouTube Data API.

2. **Running the Script**:
   - Set up your environment variables in a `.env` file:
     - `API_KEY=your_youtube_api_key`
   - Run the script:
   ```bash
   python youtube_scraper.py
   ```
   - When prompted, enter the genre ID for which you want to fetch videos.

   <body>
    <h4>YouTube Genre IDs</h4>
    <p>This table lists YouTube genre IDs that can be used with the YouTube Data API.</p>
    <table>
        <thead>
            <tr>
                <th>Genre</th>
                <th>Genre ID</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>Film & Animation</td><td>1</td></tr>
            <tr><td>Autos & Vehicles</td><td>2</td></tr>
            <tr><td>Music</td><td>10</td></tr>
            <tr><td>Pets & Animals</td><td>15</td></tr>
            <tr><td>Sports</td><td>17</td></tr>
            <tr><td>Short Movies</td><td>18</td></tr>
            <tr><td>Travel & Events</td><td>19</td></tr>
            <tr><td>Gaming</td><td>20</td></tr>
            <tr><td>Videoblogging</td><td>21</td></tr>
            <tr><td>People & Blogs</td><td>22</td></tr>
            <tr><td>Comedy</td><td>23</td></tr>
            <tr><td>Entertainment</td><td>24</td></tr>
            <tr><td>News & Politics</td><td>25</td></tr>
            <tr><td>How-to & Style</td><td>26</td></tr>
            <tr><td>Education</td><td>27</td></tr>
            <tr><td>Science & Technology</td><td>28</td></tr>
            <tr><td>Nonprofits & Activism</td><td>29</td></tr>
            <tr><td>Movies</td><td>30</td></tr>
            <tr><td>Anime/Animation</td><td>31</td></tr>
            <tr><td>Action/Adventure</td><td>32</td></tr>
            <tr><td>Classics</td><td>33</td></tr>
            <tr><td>Comedy</td><td>34</td></tr>
            <tr><td>Documentary</td><td>35</td></tr>
            <tr><td>Drama</td><td>36</td></tr>
            <tr><td>Family</td><td>37</td></tr>
            <tr><td>Foreign</td><td>38</td></tr>
            <tr><td>Horror</td><td>39</td></tr>
            <tr><td>Sci-Fi/Fantasy</td><td>40</td></tr>
            <tr><td>Thriller</td><td>41</td></tr>
            <tr><td>Shorts</td><td>42</td></tr>
            <tr><td>Shows</td><td>43</td></tr>
            <tr><td>Trailers</td><td>44</td></tr>
        </tbody>
    </table>
</body>

### Captions Script

1. **Initialization**: 
   - The script reads video URLs from a CSV file named `YOUR.csv`.
   - It fetches captions for each video and saves the results to `YOUR_CAPTION.csv`.

2. **Running the Script**:
   - Ensure you have a CSV file named `YOUR.csv` {optained in Scripting process} with the following columns:
     - `Video URL`: The URL of the YouTube video.
     - `Title`: The title of the video.
   - Run the script:
   ```bash
   python captions.py
   ```



## ⚠️ Requirements

Ensure you have:
- All required API keys in your `.env` file.
- Installed all dependencies from `requirements.txt`.

## 🛠️ Installation Steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/abhashgoyal/Youtube_Data_Study.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate # Windows
   ```
   ```bash
   source venv/bin/activate # Linux/Mac
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file with:
     - `API_KEY=your_youtube_api_key`

5. Run the application:
   ```bash
   python youtube_scraper.py
   ```

## 📊 Output Examples

The system provides:

* Captions data in `YOUR_captions.csv`
* Video details in `YOUR.csv`

## 🔒 Error Handling

* API connection validation
* Data availability checking
* Comprehensive error logging

## 🚧 Future Roadmap

* Implement additional features for data analysis
* Enhance error handling and logging mechanisms
* Add support for more video platforms

## 🛡️ License:

This project is licensed under the MIT License.

## 💖 Like my work?

This project needs a ⭐️ from you. Don't forget to leave a star ⭐️!

## 🙏 Acknowledgments

* YouTube Data API for video data
* YouTube Transcript API for captions
* Python community for excellent libraries

Developed with ❤️ by Abhash Goyal  (https://www.linkedin.com/in/abhashgoyal-4692b91b8/)
<p>abhashgoyal200@gmail.com</p>