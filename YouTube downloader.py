from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import sys

# https://www.youtube.com/watch?v=bxIcVP3YPRM
def youtube_download(URL,directory):
    yt = YouTube(f'{URL}')
    yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(output_path=directory)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"selected folder: {folder}")
    return folder

root = tk.Tk()
root.withdraw()

video_url = input("Please input a YouTube URL: ")
while True:
    root.wm_attributes('-topmost', 1)
    save_dir = open_file_dialog()
    if save_dir:
        print("Download started...")
        youtube_download(video_url, save_dir)
        print(f'Download finished! File was saved in "{save_dir}" path')
        break
    else:
        while True:
            Q = input("Invalid save location. Do you wish to try again?(Y/N) ").upper()
            if Q == "Y":
                break
            elif Q == "N":
                sys.exit()
            else:
                print("Please input correct answer.")
        
