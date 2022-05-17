from pathlib import Path
from tkinter import *
import pyperclip
import pytube.exceptions
from pytube import YouTube
from tkinter import filedialog as fd, messagebox

"""
    17May2022 - Pytube has been updated and this code is working once again
"""


def download_video():
    try:
        progress_label.config(text="Please wait")
        website = str(website_input.get())
        yt = YouTube(f"{website}")
        yt_video = yt.streams.get_highest_resolution()
        file_size = round((yt_video.filesize / 1000000), 2)
        yt_video.download(directory_name)
        progress_label.config(text=f"{file_size}mb downloaded to {directory_name}")
        print(f"{file_size} mb")
    except pytube.exceptions.AgeRestrictedError as error:
        messagebox.showerror("Error", f"{error}")
    except pytube.exceptions.ExtractError:
        messagebox.showerror("Error", "Please check the URL")
    except pytube.exceptions.HTMLParseError:
        messagebox.showerror("Error", "HTML could not be parsed")
    except pytube.exceptions.LiveStreamError:
        messagebox.showerror("Error", "Video is a live stream")
    except pytube.exceptions.MaxRetriesExceeded:
        messagebox.showerror("Error", "Maximum number of retries exceeded")
    except pytube.exceptions.MembersOnly:
        messagebox.showerror("Error", "Video is members-only")
    except pytube.exceptions.VideoPrivate:
        messagebox.showerror("Error", "Video is private")
    except pytube.exceptions.VideoRegionBlocked:
        messagebox.showerror("Error", "Video is region blocked")
    except pytube.exceptions.VideoUnavailable:
        messagebox.showerror("Error", "Base video unavailable error")
    except pytube.exceptions.PytubeError:
        messagebox.showerror("Error", "Please check the URL and try again")
    except:
        messagebox.showerror("Error", "There has been an unexpected error. Please try again")


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
