from pathlib import Path
from tkinter import *
import pyperclip
import pytube.exceptions
from pytube import YouTube
from tkinter import filedialog as fd, messagebox

"""
    24April2022: this code isn't working at the moment. according to pytube's issues tracker on Github, YouTube
    changed their code and the cipher.py file needs to be changed until pytube's developer can update
    the library
"""


def download_video():
    try:
        website = str(website_input.get())
        yt = YouTube(f"{website}")
        yt_video = yt.streams.get_highest_resolution()
        yt.register_on_progress_callback(progress_check)
        yt_video.download(directory_name)
        print(yt_video.filesize)
        return yt_video.filesize
    except pytube.exceptions.PytubeError:
        # Todo - add different exceptions. this is just a general exception that doesn't help much
        messagebox.showerror("Error", "Please check the URL")


def progress_check(stream, chunk, bytes_remaining):
    # Todo - yeah, this is goofy with the download_video() returning the file size. going to redo this
    progress_label.config(text=f"Downloaded {round(((download_video() - bytes_remaining) / 1000000), 2)} "
                               f"of {round((download_video() / 1000000), 2)}MB")


def paste_url():
    # clear any entry in website_input
    website_input.delete(0, END)
    # insert text into website_input
    website_input.insert(END, pyperclip.paste())


def change_file_path():
    global directory_name
    directory_name = fd.askdirectory()
    download_path_location.config(text=directory_name)


# get default user path
directory_name = str(Path.home())

window = Tk()
window.title("YouTube Downloader")
window.config(padx=10, pady=10)

download_path = Label(text="Download Path:", font=("arial", 10))
download_path.grid(column=0, row=0, sticky='e')

download_path_location = Label(text=directory_name, font=("arial", 8))
download_path_location.grid(column=1, row=0, sticky='w')

change_path_btn = Button(text="Select", width=12, command=change_file_path)
change_path_btn.grid(column=3, row=0, padx=10)

website_label = Label(text="Enter URL:", font=("arial", 10))
website_label.grid(column=0, row=1, sticky='e')

website_input = Entry(width=50)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

paste_URL_btn = Button(text="Paste URL", width=12, command=paste_url)
paste_URL_btn.grid(column=3, row=1, padx=10)

generate_download_btn = Button(text="Download", width=12, command=download_video)
generate_download_btn.grid(column=0, row=2, columnspan=4)

progress_label = Label(text=f"Waiting To Download", font=("arial", 10))
progress_label.grid(column=0, row=3, columnspan=4)

window.mainloop()
