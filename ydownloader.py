from pytube import YouTube

try:
    link = input("Enter Youtube Video link: ") # Enter the link
    yt = YouTube(link) # Get the video

    print("\nVideo Details: ")
    print("\nLoading...")
    print("\nTitle: ", yt.title) # Get the title
    print("Duration: ", yt.length) # Get the duration
    print("Views: ", yt.views) # Get the views
    print("Rating: ", yt.rating) # Get the rating
    print("Author: ", yt.author) # Get the author

    ys = yt.streams.get_highest_resolution() # Get the highest resolution
    print(ys)

    choice = input("\nDownload Video? (y/n): ")
    if choice == "y":
        print("\nDownloading: ", ys.default_filename) # Get the filename
        # print("Downloading...") 
        ys.download("Downloads") # Download the video in the "Downloads" folder
        print("\nDownloaded!!")
    else:
        print("\nExiting...") # Exit the program
        exit()
except Exception as e:
    print("\nInvalid Link")
    exit()


