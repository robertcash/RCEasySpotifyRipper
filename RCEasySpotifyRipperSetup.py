import os
import sys

if(sys.argv[1]):
    os.system('sudo /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    os.system('sudo easy_install pip')
    os.system('sudo brew install pyenv')
    os.system('eval "$(pyenv init -)"')
    os.system('echo 'if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi' >> ~/.bash_profile')
    os.system('pyenv install 2.7.10')
    os.system('pyenv global 2.7.10')
    os.system('brew install mopidy/mopidy/libspotify')
    os.system('sudo ln -s /usr/local/opt/libspotify/lib/libspotify.12.1.51.dylib \
        /usr/local/opt/libspotify/lib/libspotify')
    os.system('sudo brew install lame')
    os.system('sudo pip install mutagen')
    os.system('sudo pip install colorama')
    os.system('python setup.py install')
    os.system('pyenv rehash')

    print 'Please go here to get an application key: https://devaccount.spotify.com/my-account/keys/'
    print 'You must have a Spotify Premium Account to do this.'
    print 'Make an application on there and download the Binary key by clicking "Binary"'
    print 'Move "spotify_appkey.key" to this folder.'

else:
    print 'Please enter python RCEasySpotifyRipperSetup.py'