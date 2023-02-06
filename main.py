from pytube import YouTube

def Download(link):
   youtubeObject = YouTube(link)
   youtubeObject = youtubeObject.streams.get_highest_resolution()
   try:
      youtubeObject.download()
   except:
      print("There has been an error in downloading your YouTube video.")
      print("This download has been completed!")