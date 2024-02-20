# video_processing.py

import os
import random
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, ColorClip

def list_video_files(directory):
    """List all video files in a directory."""
    return [f for f in os.listdir(directory) if f.lower().endswith(('.mov', '.mp4'))]

def select_random_files(files, num_to_select):
    """Select a random subset of files."""
    if len(files) < num_to_select:
        raise ValueError(f"Not enough files to select {num_to_select}.")
    return random.sample(files, num_to_select)

def calculate_target_duration(total_duration, proportion, num_videos):
    """Calculate target duration for each video clip in a category."""
    # First, calculate the total duration for the category
    total_category_duration = (proportion / 100) * total_duration

    # Then, divide this total duration by the number of videos in the category
    return total_category_duration / num_videos

def trim_clip(clip, target_duration):
    """Trim the clip to the target duration."""
    return clip.subclip(0, min(target_duration, clip.duration))

def adjust_duration_for_beat(clip_start_time, ideal_duration, remaining_category_duration, beat_times, MINIMUM_CLIP_DURATION):
    ideal_end_time = clip_start_time + ideal_duration
    valid_beats = [beat for beat in beat_times if clip_start_time < beat < clip_start_time + remaining_category_duration]

    closest_beat_time = min(valid_beats, key=lambda beat: abs(beat - ideal_end_time), default=None)

    if closest_beat_time:
        adjusted_duration = max(closest_beat_time - clip_start_time, MINIMUM_CLIP_DURATION)
    else:
        adjusted_duration = min(ideal_duration, remaining_category_duration)

    print(f"Clip Start: {clip_start_time}, Ideal End: {ideal_end_time}, Closest Beat: {closest_beat_time}, Adjusted Duration: {adjusted_duration}")

    return adjusted_duration


def process_file(file, category_path, target_duration):
    clip_path = os.path.join(category_path, file)
    clip = VideoFileClip(clip_path)
    trimmed_clip = trim_clip(clip, target_duration)
    return trimmed_clip, clip  # Return both


def process_category(category, category_path, num_videos, total_proportion, original_total_duration, all_clips, original_clips, beat_times, current_duration, MINIMUM_CLIP_DURATION, USE_ALL_CLIPS):
    remaining_category_duration = (total_proportion / 100) * original_total_duration  # Total duration for this category
    category_duration_used = 0  # Track how much of the category's duration has been used

    video_files = list_video_files(category_path)

    # Select files based on USE_ALL_CLIPS
    if USE_ALL_CLIPS:
        selected_files = video_files  # Use all files
    else:
        selected_files = select_random_files(video_files, num_videos)

    selected_files = select_random_files(video_files, num_videos)

    for file in selected_files:
        # Calculate the ideal target duration for this clip
        ideal_target_duration = calculate_target_duration(original_total_duration, total_proportion, num_videos)

        # Check if the remaining category duration is less than the ideal target duration
        if remaining_category_duration - category_duration_used < ideal_target_duration:
            ideal_target_duration = remaining_category_duration - category_duration_used

        # Adjust the duration to align with the nearest beat, if possible
        adjusted_duration = adjust_duration_for_beat(current_duration, ideal_target_duration, remaining_category_duration - category_duration_used, beat_times, MINIMUM_CLIP_DURATION)

        # Process the file with adjusted duration
        trimmed_clip, clip = process_file(file, category_path, adjusted_duration)
        all_clips.append(trimmed_clip)
        original_clips.append(clip)

        # Update the current duration and the used category duration
        current_duration += adjusted_duration
        category_duration_used += adjusted_duration

        # Break if the category's total duration has been used up
        if category_duration_used >= remaining_category_duration:
            break

    return current_duration



def advanced_concatenate(base_video_dir, categories, folder_settings, total_duration, output_path, beat_times, audio_clip, MINIMUM_CLIP_DURATION, USE_ALL_CLIPS):
    all_clips = []
    original_clips = []  # List to store original clips
    current_duration = 0
    log_filename = "video_concatenation_log.txt"

    with open(log_filename, "a") as log_file:
        log_file.write("Concatenation session:\n")

        for category in categories:
            num_videos, total_proportion = folder_settings[category]
            category_path = os.path.join(base_video_dir, category)
            current_duration = process_category(category, category_path, num_videos, total_proportion, total_duration, all_clips, original_clips, beat_times, current_duration, MINIMUM_CLIP_DURATION, USE_ALL_CLIPS)

        log_file.write("End of session\n\n")

    # Extend the last clip to match the total duration if necessary
    all_clips = extend_last_clip(all_clips, total_duration)

    # Concatenate all clips to form the final clip
    final_clip = concatenate_videoclips(all_clips)

    # Set the audio of the final video clip to match the specified total duration
    final_clip = final_clip.set_audio(audio_clip.set_duration(total_duration))

    # Output the concatenated video with extended last clip and audio
    final_clip.write_videofile(output_path, codec="libx264", fps=24, ffmpeg_params=['-crf', '18', '-aspect', '9:16'])

    # Close all original clips
    for clip in original_clips:
        clip.close()

        
def extend_last_clip(all_clips, total_duration):
    """
    Extend the last clip in the list to make the total duration of all clips
    match the total_duration specified.
    """
    final_clip_duration = sum([clip.duration for clip in all_clips])
    additional_duration = total_duration - final_clip_duration

    if additional_duration > 0 and all_clips:
        # The last clip needs to be extended to fill the remaining time
        last_clip = all_clips[-1]
        # Calculate the new end time for the last clip
        last_clip_end = last_clip.end + additional_duration
        # Create a new clip with the extended duration
        extended_last_clip = last_clip.set_duration(last_clip.duration + additional_duration)
        # Replace the last clip with the extended clip
        all_clips[-1] = extended_last_clip

    return all_clips

