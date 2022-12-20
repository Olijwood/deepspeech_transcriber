from pydub import AudioSegment
import os

def main():
    cwd = os.getcwd()
    for file in os.listdir(f'{cwd}/audio_files/'):
        if file.endswith('.wav'):
            raw_audio = AudioSegment.from_file(f'/Users/Oli/DeepSpeech/audio_files/{file}', format="wav")
            raw_audio.export(f"{cwd}/processed_audio/{file.rstrip('.wav') + '_processed.wav'}_processed.wav", format="wav", codec="pcm_s16le", parameters=["-ac", "1", '-ar', '16000', '-b:a', '256k'])