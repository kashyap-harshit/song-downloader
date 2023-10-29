import pytube
import glob
import os
from moviepy.editor import AudioFileClip

playlist = pytube.Playlist("https://www.youtube.com/playlist?list=PLgQt1Non252yzE4jAjmbQktrJCdM6GO9_")

download_path = "E:\\Files\\song downloading\\songs"


all_files =glob.glob(f"E:\\Files\\song downloading\\songs\\*.mp3")

for url in playlist:
    video = pytube.YouTube(url)
    video_title = ""
    for j in video.title: #was facing some kind of an error if the song title had some special characters so modifying the title
        if j.isalpha() or j == " " or j.isalnum():
            video_title += j
    print(f"downloading {video_title}")
    video_loc = f"E:\\Files\\song downloading\\beatles_100\\{video_title}.mp3"
    if video_loc in all_files:
        print("file already found \n downloading next song\n")
        continue
    try:
        stream = video.streams.get_audio_only()
        stream.download(output_path=download_path, filename=f"{video_title}.mp4")
        video_path = os.path.join(download_path, f"{video_title}.mp4")
        audio_path = os.path.join(download_path, f"{video_title}.mp3")
        
        audio_clip = AudioFileClip(video_path)
        audio_clip.write_audiofile(audio_path)
        os.remove(download_path + f"\\{video_title}.mp4")
    except Exception as e:
        print("could not download\n", e)