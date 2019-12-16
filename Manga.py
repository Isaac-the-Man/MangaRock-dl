import requests
import json
import sys
from Chapter import Chapter
import os


class Manga:

    # constructor
    def __init__(self, oid):
        self.OID = oid
        self.VERSION = '401'
        self.NAME = None
        self.MANGA_API = f'https://api.mangarockhd.com/query/web{self.VERSION}/info?oid=mrs-serie-{self.OID}&last=0'
        self.data = None
        self.chapterList = {}

    # get json
    def getData(self):
        try:
            self.data = json.loads(requests.get(self.MANGA_API).text)
        except:
            print('Error Occured While Running API...')
            sys.exit()
        self.NAME = self.data['data']['name']
        print('Manga \'{}\' Loaded'.format(self.NAME))

    # parse to chapter objects
    def parseChapters(self):
        for ch in self.data['data']['chapters']:
            chapter = Chapter(ch['oid'][12:], ch['order'], ch['name'])
            print('Index: {} --- {}'.format(chapter.INDEX, chapter.NAME))
            self.chapterList[chapter.INDEX] = chapter

    # download chapters
    def download(self, path, chapters = 'all', format='webp'):
        self._createDir(path + self.NAME + '/')
        if (chapters == 'all'):
            for ch in self.chapterList:
                chapter = self.chapterList.get(ch)
                chapter.getData()
                chapter.download(path + self.NAME + '/', format=format)
        else:
            for ch in chapters:
                chapter = self.chapterList.get(ch)
                chapter.getData()
                chapter.download(path + self.NAME + '/', format=format)

    # create folder
    def _createDir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
