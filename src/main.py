import random
import time
import os
from moviepy.editor import AudioFileClip  # Import AudioFileClip
import video_processing
import audio_processing

# Seed the random number generator with current time
random.seed(time.time())

# Constants for the number of videos to select from each folder
NUM_VIDEOS_B_ROLL = 5
NUM_VIDEOS_ACTION_TRANSITION = 3
NUM_VIDEOS_CONCLUSION = 4
NUM_VIDEOS_INTRODUCTION = 3
NUM_VIDEOS_BODY = 15

# Constants for the proportion of each category
PROPORTION_B_ROLL = 20  # Percentage
PROPORTION_ACTION_TRANSITION = 20
PROPORTION_CONCLUSION = 20
PROPORTION_INTRODUCTION = 20
PROPORTION_BODY = 20

# MINIMUM_CLIP_DURATION = .1
MINIMUM_CLIP_DURATION = 0

USE_ALL_CLIPS = False

# Ask the user for the total duration of the video clip
try:
    TOTAL_DURATION = float(input("Enter the total duration for the video clip in seconds: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

base_export_dir = os.path.join(os.path.dirname(__file__), '..', 'exports')
# Ensure the exports directory exists
if not os.path.exists(base_export_dir):
    os.makedirs(base_export_dir)

base_video_dir = os.path.join(os.path.dirname(__file__), '..', 'video_clips')
base_audio_dir = os.path.join(os.path.dirname(__file__), '..', 'audio_clips')
base_img_dir = os.path.join(os.path.dirname(__file__), '..', 'img')

# File path for the input audio
# input_audio = os.path.join(base_audio_dir, "boat party reel audio example 002.wav")
input_audio = os.path.join(base_audio_dir, "boat party reel audio example 003.wav")
# input_audio = os.path.join(base_audio_dir, "reel_audio_example_001.wav")

cropped_output_audio_path = os.path.join(base_export_dir, "cropped_audio_example.mp3")  # Adjusted path

# Crop the audio to match the total duration
audio_processing.crop_audio(input_audio, cropped_output_audio_path, TOTAL_DURATION)

# Load the cropped audio file
cropped_audio_clip = AudioFileClip(cropped_output_audio_path)

# Detect beats in the audio file
beat_times = audio_processing.detect_beats(input_audio, TOTAL_DURATION)

# Categories and settings for video processing
categories = ['introduction', 'b_roll', 'body', 'action_transition', 'conclusion']
folder_settings = {
    'b_roll': (NUM_VIDEOS_B_ROLL, PROPORTION_B_ROLL),
    'action_transition': (NUM_VIDEOS_ACTION_TRANSITION, PROPORTION_ACTION_TRANSITION),
    'conclusion': (NUM_VIDEOS_CONCLUSION, PROPORTION_CONCLUSION),
    'introduction': (NUM_VIDEOS_INTRODUCTION, PROPORTION_INTRODUCTION),
    'body': (NUM_VIDEOS_BODY, PROPORTION_BODY)
}

output_video_path = os.path.join(base_export_dir, "output.mov")
# Creating and outputting our video to exports with the cropped audio
video_processing.advanced_concatenate(base_video_dir, categories, folder_settings, TOTAL_DURATION, output_video_path, beat_times, cropped_audio_clip, MINIMUM_CLIP_DURATION, USE_ALL_CLIPS)

# Close the audio clip
cropped_audio_clip.close()

print("Detected Beat Times:", beat_times)
