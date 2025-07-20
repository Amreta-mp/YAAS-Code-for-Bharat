from moviepy.editor import *
from gtts import gTTS
import os
import tempfile

def text_to_video(script, output_path="output_video.mp4"):
    # Split script into chunks
    slides = script.split("\n\n")

    clips = []

    for i, slide_text in enumerate(slides):
        # Convert slide text to audio using gTTS
        tts = gTTS(slide_text)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            audio = AudioFileClip(fp.name)

        # Create text clip
        text_clip = TextClip(slide_text, fontsize=24, color='white', size=(1280, 720), method='caption', align='center')
        text_clip = text_clip.set_duration(audio.duration).set_audio(audio).set_position('center').on_color(size=(1280, 720), color=(0, 0, 0), col_opacity=1)

        clips.append(text_clip)

    # Concatenate all
    final = concatenate_videoclips(clips, method="compose")
    final.write_videofile(output_path, fps=24)

# Sample usage
if __name__ == "__main__":
    with open("script.txt", "r", encoding="utf-8") as f:
        full_script = f.read()
    text_to_video(full_script)
