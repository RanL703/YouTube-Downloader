# YouTube-Downloader
We are going to download a YouTube video using pytube module in python.
Code structure:
1. First install the pytube module using the method in this [link](https://pytube.io/en/latest/user/install.html).
2. After that go and import the YouTube module from pytube.
3. Then use "try" and define a variable to enter the YouTube link you want to download out of.
4. Then convert the link into a YouTube object using the YouTube() function.
5. Extract the highest resolution using the .streams.get_highest_resolution() function.
6. Then download the video to the directory using .download function.
7. Make an exception for any error that might show up.
