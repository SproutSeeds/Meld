# audio_processing.py

from pydub import AudioSegment
import librosa

def crop_audio(audio_file, output_file, total_duration):
    """
    Crop the audio file to match the total_duration.

    :param audio_file: Path to the input audio file
    :param output_file: Path to save the cropped audio file
    :param total_duration: Total duration in seconds
    """
    audio = AudioSegment.from_file(audio_file)
    total_duration_mili = total_duration * 1000
    cropped_audio = audio[:total_duration_mili]
    cropped_audio.export(output_file, format="wav")

def detect_beats(audio_file, duration=10):
    """
    Detect beats in the first 'duration' seconds of an audio file.
    
    :param audio_file: Path to the audio file
    :param duration: Duration in seconds to analyze (default is 10 seconds)
    :return: List of beat times in seconds
    """
    y, sr = librosa.load(audio_file, duration=duration)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beats, sr=sr)
    return beat_times
