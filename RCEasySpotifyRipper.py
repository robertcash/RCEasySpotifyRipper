import os
import re
import sys

fin = open('spotify_list.txt')

try:
    username = sys.argv[1]
    password = sys.argv[2]

    RE_GET_ID = re.compile('.*track\/(.*)')
    print 'go'

    for line in fin:
        print line
        id_match = RE_GET_ID.match(line)
        print id_match
        if id_match:
            cmd = 'spotify-ripper -u'+username+' -p'+ password +' spotify:track:'+ id_match.group(1)+' -k spotify_appkey.key'
            os.system(cmd)

    fin.close()

except:
    print 'No username and/or password. Please type python RCEasySpotifyRipper.py USERNAME PASSWORD'