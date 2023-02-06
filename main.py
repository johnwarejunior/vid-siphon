from pytube import YouTube

def Download(link):
   youtubeObject = YouTube(link)
   youtubeObject = youtubeObject.streams.get_highest_resolution()
   try:
      youtubeObject.download()
      print("This download has been completed!")
   except:
      print("There has been an error in downloading your YouTube video.")
      

   link = input("Insert YouTube link.")
   Download(link)