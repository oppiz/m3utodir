import sys
import os
import urllib.parse

from shutil import copyfile

# python pl-copy.py all.m3u E:\music\
def main():
    #uncomment if you wnat to fun from command line
    #if len(sys.argv) < 3:
    #    return 1

    #playlist_file = sys.argv[1]
    #output_dir = sys.argv[2]

    #Comment out if running from command line
    playlist_file = r"C:\Users\zippo\Desktop\FinalPlaylist.m3u"
    output_dir = r"C:\Users\zippo\Desktop\MUSIC"

    if os.path.exists(output_dir) & os.path.exists(playlist_file): 
        print("all is good")
        with open(playlist_file, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    # Skip m3u comments
                    continue
                else:
                    nle = line.rstrip()
                    nle = urllib.parse.unquote(nle) #Parse UTF-8 
                    nle = nle[5:] #Remove leading "File:"
                    #print(nle)
                    basename = os.path.basename(nle)
                    print("copying file %s..." % (basename,))
                    dst = os.path.join(output_dir, basename)
                    copyfile(nle, dst)

        return 0
    elif not os.path.exists(output_dir) and os.path.exists(playlist_file): 
        print("Output DIR %s does not exist" % (output_dir))
        return 1
    elif os.path.exists(output_dir) and not os.path.exists(playlist_file):
        print("Input playlist %s does not exist" % (playlist_file))
        return 1
    else:
        print("Playlist and output DIR do not exist")
        return 1

if __name__ == "__main__":
    sys.exit(main())
