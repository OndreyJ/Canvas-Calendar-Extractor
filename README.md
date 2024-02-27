# Canvas Calendar Extractor

## Description
This Python script extracts calendar files from favorited courses in Canvas, allowing users to use them elsewhere.

## Prerequisites
Ensure Python is installed on your device.

## Usage
1. Navigate to Canvas:
    - Click the account icon on the top left of the screen.
    - Click "Settings."
    - Scroll down and find "New Access Token" and click it.
    - Give it a name and click "Generate Token." (WARNING: Do not share this token with anyone as it is used to log into your account!)
    - Copy the token and paste it into "OpenMe.txt" (Keep the single quotes around the token).
    - Copy the subdomain of your Canvas URL and paste it into "OpenMe.txt" (This is usually your College's abbreviation and is before ".instructure") (Keep the single quotes around the token).
2. Run the script:
    - Right-click "FetchCanvasCalendars.py" => Open with => Python.

## Video Demonstration


Click the thumbnail to watch a video demonstration of the script in action.

## Output
The extracted calendar files will be saved in a folder created by the script. These files can be used on various platforms.

## Note
Make sure to create a separate Courses Calendar for these files, as most platforms will require you to delete these individual events manually if you no longer want to see them.
