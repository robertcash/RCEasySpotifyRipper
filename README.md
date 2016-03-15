# RCEasySpotifyRipper

RCEasySpotifyRipper is a Python script that easily rips Spotify MP3's built on top of [spotify-ripper](https://github.com/jrnewell/spotify-ripper). Mac OS only supported.

## How to use

1. Download .zip file above.

2. Open Terminal and enter:

  cd Downloads/RCEasySpotifyRipper
  
3. Enter the follow line in terminal to setup spotify-ripper, or do it [manually](https://github.com/jrnewell/spotify-ripper):

  python RCEasySpotifyRipperSetup.py install
  
4. As indicated in the last few lines printed in the setup program. You must go to https://devaccount.spotify.com/my-account/keys/ to get an application key. You must have a Spotify Premium account to do so. After you make an application and download the Binary key, put the file "spotify_appkey.key" into the folder with the rest of the files of RCEasySpotifyRipper.

5. Edit spotify_list.txt by adding a url to each line to download any number of desired tracks:
  
  https://play.spotify.com/track/275a9yzwGB6ncAW4SxY7q3
  https://play.spotify.com/track/2cgZfcnb639TaZhd1AU8iz

6. Type in the following into the terminal and enjoy:
  
  python RCEasySpotifyRipper.py YOURUSERNAME YOURPASSWORD

## Note

  You must change directory in terminal to wherever the RCEasySpotifyRipper folder is to use RCEasySpotifyRipper.py. For   example, if RCEasySpotifyRipper foler is in documents, enter cd Documents/RCEasySpotifyRipper and enter the usual command python RCEasySpotifyRipper.py YOURUSERNAME YOURPASSWORD. 

