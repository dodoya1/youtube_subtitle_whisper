import whisper
from datetime import timedelta
from srt import Subtitle
from deep_translator import GoogleTranslator
import srt
import os

# Insert a line break when the number of characters in a line reaches 21.
def add_line(s):
    new_s = ""
    line_len = 0
    for char in s:
        if line_len == 21:
            new_s += "\n"
            line_len = 0
        new_s += char
        line_len += 1
    return new_s

# Embed subtitles in videos
def embed_subtitles(result_folder_path):
    # Convert SRT file to ASS file
    os.system(f"ffmpeg -i {result_folder_path}/target.srt {result_folder_path}/target.ass")
    # Embed subtitles in video
    os.system(f"ffmpeg -i {result_folder_path}/target.mp4 -vf ass={result_folder_path}/target.ass {result_folder_path}/output.mp4")

# Use GoogleTranslator module to translate text into Japanese
def translate(text, translated_lang):
    translated = GoogleTranslator(source = 'auto',target = translated_lang).translate(text)
    return translated

# Download the video from the given YouTube URL.
def yt_download(URL, result_folder_path):
    path = f"{result_folder_path}/target.mp4"
    # Download the video
    os.system(f"yt-dlp -f best -v {URL} -o {path}")

# Generate subtitles.
def generate_subtitles(result, result_folder_path, translated_lang):
    segments = result["segments"]
    subs = []

    # Iterate over the segments and create SRT subtitles for each segment.
    for data in segments:
        index = data["id"] + 1
        start = data["start"]
        end = data["end"]
        # Translate the segment text to the desired language.
        translated_text = translate(data["text"], translated_lang)

        # Add line breaks to the translated text to improve readability.
        text = add_line(translated_text)

        # Create an SRT subtitle object.
        sub = Subtitle(index = 1, start = timedelta(seconds = timedelta(seconds = start).seconds,
                                                microseconds = timedelta(seconds = start).microseconds),
                    end = timedelta(seconds = timedelta(seconds = end).seconds,
                                    microseconds = timedelta(seconds = end).microseconds), content = text, proprietary = '')

        # Append the subtitle to the list of subtitles.
        subs.append(sub)
    
    # Write the SRT file to disk.
    with open(result_folder_path + "/target.srt", mode = "w", encoding = "utf-8") as f:
        f.write(srt.compose(subs))

def main():
    URL = input("Enter the YouTube URL to which you want to add subtitles:")
    translated_lang = input("Please enter the subtitle language (language after translation):")
    result_folder_name = str(input("Specify the name of the folder in which to save the output results:"))

    # Folder name to save output results
    result_folder_path = f"./result/{result_folder_name}"
    os.mkdir(result_folder_path)

    # Download the YouTube video using the yt_dl module.
    yt_download(URL, result_folder_path)

    model = whisper.load_model("medium")
    result = model.transcribe(f"{result_folder_path}/target.mp4")

    # Save the transcription as a text file.
    with open(f"{result_folder_path}/transcript.txt", mode = "w") as f:
        f.write(result["text"])

    # Generate subtitles.
    generate_subtitles(result, result_folder_path, translated_lang)

    # Use the ffmpeg command to add the SRT subtitles to the video.
    embed_subtitles(result_folder_path)

if __name__ == "__main__":
    main()
    