from pytube import YouTube

try:
    # to input the YouTube link
    URL = input("Enter the YouTube link:")
    
    yt = YouTube(URL)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # extract the highest resolution of the stream
    d = yt.streams.get_highest_resolution()
    
    # downloading to the directory
    d.download()
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))
