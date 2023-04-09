# YouTube Subtitle Whisper

<br>
    <div>
        <a href="https://colab.research.google.com/github/dodoya1/youtube_subtitle_whisper/blob/master/tutorial.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
    </div>
<br>

## Description
"YouTube Subtitle Whisper" is a Python script for adding subtitles to YouTube videos. Users can enter the URL of the YouTube video they wish to add subtitles to and enter the subtitle language. Thus, native Japanese speakers can input the URL of a YouTube video in English and select Japanese as the subtitle language to watch the video without any language barrier.

## Setup
Install this repository with the following command:

    git clone https://github.com/dodoya1/youtube_subtitle_whisper.git

In order to execute this code, the required modules must be installed:

    pip install -r requirements.txt

It also requires the command-line tool [`ffmpeg`](https://ffmpeg.org/) to be installed on your system, which is available from most package managers:

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

## Usage
Execute main.py with the following command.

    python3 main.py

Next, enter the URL of the YouTube video to which you want to add subtitles and enter the language of the subtitles. In addition, you will need to enter the name of the folder where you want to save the output results.

When selecting a language, please refer to the "ISO-639 Code" on the following website.

https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

## Approach
This Python script allows the user to download a video from a given YouTube URL, transcribe the speech in the video using the whisper library, translate the transcription into a desired language using the deep_translator library, and embed the translated subtitles into the video using ffmpeg. The approach followed by the script can be summarized as follows:

1. The user is prompted to enter the YouTube URL and the desired language for the subtitles.
2. The video is downloaded using the yt-dlp module.
3. The whisper library is used to transcribe the speech in the video, and the transcription is saved as a text file.
4. The deep_translator library is used to translate the transcription into the desired language.
5. The translated text is formatted with line breaks to improve readability.
6. An SRT subtitle object is created for each segment of the transcription.
7. The SRT subtitles are written to a file.
8. The ffmpeg command is used to convert the SRT subtitles to ASS format and embed them into the video.
9. The output video with embedded subtitles is saved as output.mp4.

## References
https://self-development.info/%E3%80%90python%E3%80%91ai%E9%9F%B3%E5%A3%B0%E8%AA%8D%E8%AD%98whisper%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9Fsrt%E5%AD%97%E5%B9%95%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E8%87%AA%E5%8B%95%E4%BD%9C/

https://self-development.info/%E3%80%90%E7%84%A1%E6%96%99%E3%83%BB%E7%B0%A1%E5%8D%98%E3%80%91ffmpeg%E3%81%AB%E3%82%88%E3%82%8B%E5%8B%95%E7%94%BB%E3%81%B8%E3%81%AE%E5%AD%97%E5%B9%95%E3%83%BB%E6%96%87%E5%AD%97%E5%85%A5%E3%82%8C/

https://github.com/openai/whisper

https://tt-tsukumochi.com/archives/2028

## Contribute
Please share your ideas and opinions!	
### Bug Report
If you find a bug in the project, please submit a detailed bug report on the Issues page on Github. Please include steps to reproduce the problem, expected behavior, and actual behavior. Screenshots and error messages are also helpful.
### Feature Requests
If you have an idea for a new feature, please submit a feature request on the Issues page on Github. Please describe the feature in detail and how it will benefit the project. If possible, please provide examples or mockups.
### Pull Requests
We welcome pull requests from anyone who would like to contribute to the project. Fork the repository and create a new branch for your changes. Please ensure that your code conforms to our coding standards and include unit tests where appropriate. Once you submit a pull request, it will be reviewed by a maintainer.
### Documentation
We need help improving our project documentation. This includes adding to the README.md file, creating user guides, and updating inline code comments. To contribute to the documentation, please submit a pull request with your changes.
### Evaluation
We value the contributions of all contributors highly. If you submit a pull request and it is merged into the project, we will add you to the list of contributors in the README.md file. Additionally, if you contribute significantly to the project, we may invite you to become a maintainer.
