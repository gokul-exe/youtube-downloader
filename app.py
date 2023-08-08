from flask import Flask, render_template, request, send_file, Response

from io import BytesIO
from pytube import YouTube

app = Flask(__name__)


def download_audio_or_video(url, download_type):
    try:
        yt = YouTube(url)

        if download_type == "audio":
            stream = yt.streams.filter(only_audio=True).first()
            file_extension = 'mp3'
        elif download_type == "video":
            stream = yt.streams.filter(file_extension='mp4').first()
            file_extension = 'mp4'
        else:
            raise ValueError("Invalid download type. Please choose 'audio' or 'video'.")

        print(f"Downloading {download_type.capitalize()}: {yt.title}...")
        video_bytes = BytesIO()
        stream.stream_to_buffer(video_bytes)
        video_bytes.seek(0)  # Reset the buffer position to the beginning
        print("Download completed!")

        return video_bytes, yt.title + '.' + file_extension

    except Exception as e:
        print("Error:", e)
        return None

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        youtube_url = request.form["youtube_url"]
        download_type = request.form["download_type"]

        video_bytes, filename = download_audio_or_video(youtube_url, download_type.lower())

        if video_bytes:
            response = Response(video_bytes, mimetype="video/mp4")
            response.headers["Content-Disposition"] = f"attachment; filename={filename}"
            return response

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
