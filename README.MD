### Problem that we solve for a specific customer type
I have over 1000 images/videos saved in the cloud for my artistic content creation for my business. And after the event, that content is never really accessed again. This is a system where we can categorize our content, have AI detail each piece that we have and keep a growing knowledge of our video clip options based on the story that we want to tell.

### Original Project Goal
I originally made this tool to help me make a video for my friend. He had a folder of video content, I hand selected the content and dropped it into specific categories, and instead of manually cutting the clips to music, I wanted to have this be automatd. So now, whatever music you have, whatever content you are working with, all you need to do is separate it by hand into 5 categories, and this program will auto generate content for you that is following the beat of the song that it is targetting.

# Stretch Goals
- Only require a single folder for you to dump all of your content.
- Add an AI component to add description text to each video clip within out content folder and save this in a database, only having AI categorize newly added material to the singular folder.
- You name your categories, you want, the AI will parse these catgories and based on the categories/text you give it, it will choose the best video clips to use for the video creation.
- And finally creating the video in a similar fashion to how we have it being created now, but doing so in a way to give the creator more freedom and utilizing historic content they have that they may have forgotten about.


## Step 1:
 - Separate your video clips into the 5 category folders you see within the video_clips directory.
## Step 2:
- Add your music file to the audio clips folder. I have a sample of a song I made there as the default. 
- Feel free to use that, you have my permission.
- If you want to use your own audio, add it to the folder and change line 48 within main.py to point to your audio file.

# Currently pointing to my song:
input_audio = os.path.join(base_audio_dir, "boat party reel audio example 003.wav")

## Step 4:
- There are a list of constants defined at the top of main.py (line 11), you will change these based on how maany clips you want the program to use from each category.
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
- enter in the amount of time you want your final video to be **(if using my audio file, it must be 20 seconds)**s

## Step 7:
- view the outputted video within the exports folder, it will be titled output.mov, there will also be a copy of the cropepd audio sample (cropped at the inputted time you put, if 20 seconds itll be cropped at 20 seconds)
- Enjoy!




