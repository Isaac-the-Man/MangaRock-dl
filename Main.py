from Manga import Manga
import argparse


# parse range to list
def parseRange(strRange):
    newRange = []
    for r in strRange.split(','):
        if (not '-' in r):
            newRange.append(int(r))
        else:
            rs = r.split('-')
            newRange.extend(list(range(int(rs[0]), int(rs[1])+1)))
    newRange = list(dict.fromkeys(newRange))    # clear duplicate
    return sorted(newRange)

# parse argument
parser = argparse.ArgumentParser(description='Download Manga from mangarock.com')
parser.add_argument('-s', '--series', help='series OID of the manga', required=True)
parser.add_argument('-i', '--info', action='store_true', required=False)
parser.add_argument('-f', '--format', help='format of the downloaded file, default is webp, png and jpg supported', required=False)
parser.add_argument('-r', '--range', help='range of index(chapters) you want to download', required=False)
parser.add_argument('-d', '--directory', help='download destination', required=False)
args = vars(parser.parse_args())

oid = args['series']
format = args['format'] if args['format'] else 'webp'
range = parseRange(args['range']) if args['range'] else 'all'
dir = args['directory'] if args['directory'] else './'
info = args['info']

# print info only
manga = Manga(oid)
manga.getData()
manga.parseChapters()

# download
print(range)
if (not info):
    manga.download(dir, chapters=range, format=format)
