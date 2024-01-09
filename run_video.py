import subprocess, os, zipfile
VLC_PATH = r"Resources/vlc-3.0.20/vlc.exe"
VIDEO_PATH = "VIDEOS"

if not os.path.exists(VLC_PATH):
    with zipfile.ZipFile("Resources/vlc-3.0.20-win32.zip",'r') as zip_ref:
        zip_ref.extractall("Resources/")
        
if not os.path.exists(VIDEO_PATH):
    os.makedirs(VIDEO_PATH, exist_ok=True)
    
video_list = os.listdir(VIDEO_PATH)

for i, video in enumerate(video_list):
    subprocess.Popen([VLC_PATH, f"--qt-fullscreen-screennumber={i}", "--loop", "--no-video-title-show", "--fullscreen", f"{VIDEO_PATH}/{video}"])