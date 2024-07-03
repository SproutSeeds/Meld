### Original Project Goal
I originally made this tool to help me make a video for my friend. He had a folder of video content, I hand-selected the content and dropped it into specific categories, and instead of manually cutting the clips to music, I wanted to have this be automated. So now, whatever music you have, whatever content you are working with, all you need to do is separate it by hand into 5 categories, and this program will auto-generate content for you that follows the beat of the song that it is targeting.

# Stretch Goals
- Only require a single folder for you to dump all of your content.
- Add an AI component to add description text to each video clip within our content folder and save this in a database, only having AI categorize newly added material to the singular folder.
- The user names categories, the AI will parse these categories and based on the categories/text you give it, it will choose the best video clips to use for the video creation.
- Finally, creating the video in a similar fashion to how we have it being created now, but doing so in a way to allow the creator more freedom and utilize historic content they have that they may have forgotten about.


## Step 1:
 - Separate your video clips into the 5 category folders you see within the video_clips directory.
## Step 2:
- Add your music file to the audio clips folder. I have a sample of a song I made there as the default. 
- Feel free to use that, you have my permission.
- If you want to use your audio, add it to the folder and change line 48 within main.py to point to your audio file.

# Currently pointing to my song in main.py:
input_audio = os.path.join(base_audio_dir, "boat party reel audio example 003.wav")

## Step 4:
- There is a list of constants defined at the top of main.py (line 11), you will change these based on how many clips you want the program to use from each category.
- The next section of constants is to define the percentage proportionality of each category. If you have 1 from each category each clip will be 4 seconds long if the inputted final amount is 20 seconds. As you add more clips, the time gets shorter.
- Here they are:

    NUM_VIDEOS_B_ROLL = 5
    NUM_VIDEOS_ACTION_TRANSITION = 3
    NUM_VIDEOS_CONCLUSION = 4
    NUM_VIDEOS_INTRODUCTION = 3
    NUM_VIDEOS_BODY = 15

    PROPORTION_B_ROLL = 20  # Percentage
    PROPORTION_ACTION_TRANSITION = 20
    PROPORTION_CONCLUSION = 20
    PROPORTION_INTRODUCTION = 20
    PROPORTION_BODY = 20

## Step 5:
- make sure you are within the ./src folder in your command line.
- type and enter in:
    # python main.py

## Step 6:
- Enter the amount of time you want your final video to be **(if using my audio file, it must be 20 seconds)**s

## Step 7:
- view the outputted video within the exports folder, it will be titled output.mov, there will also be a copy of the cropped audio sample (cropped at the inputted time you put, if 20 seconds it'll be cropped at 20 seconds)
- Enjoy!




