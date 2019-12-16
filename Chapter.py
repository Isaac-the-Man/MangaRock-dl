import requests
import json
import struct
import os
import subprocess


class Chapter:

    # constructor
    def __init__(self, oid, index, name):
        self.OID = oid
        self.INDEX = index
        self.NAME = name
        self.VERSION = 401
        self.CHAPTER_API = f'https://api.mangarockhd.com/query/web{self.VERSION}/pages?oid=mrs-chapter-{self.OID}'
        self.data = [] # list of mri files

    # get MRI data
    def getData(self):
        raw = json.loads(requests.get(self.CHAPTER_API).text)
        for page in raw['data']:
            self.data.append(page)

    # download all webp, support conversion to png, jpg
    def download(self, path, format='webp'):
        print(f'\nDownloading Index {self.INDEX} --- {self.NAME}...')
        self._createDir(path + f'index{self.INDEX}')
        counter = 1
        for mri in self.data:
            print(f'Downloading Page {counter}/{len(self.data)}...')
            r = requests.get(mri)
            with open(path + f'index{self.INDEX}' + f'/page{counter}.webp', 'wb') as f:
                buffer = bytes(self._parse_mri_data_to_webp_buffer(r.content))
                f.write(buffer)
            if (not format == 'webp'):
                subprocess.run(['dwebp', path + f'index{self.INDEX}' + f'/page{counter}.webp', '-o', path + f'index{self.INDEX}' + f'/page{counter}.{format}'])
                os.remove(path + f'index{self.INDEX}' + f'/page{counter}.webp')
            counter += 1

    # create folder
    def _createDir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    # parse mri to webp
    def _parse_mri_data_to_webp_buffer(self, data):
        size_list = [0] * 4
        size = len(data)
        header_size = size + 7

        # little endian byte representation
        # zeros to the right don't change the value
        for i, byte in enumerate(struct.pack("<I", header_size)):
            size_list[i] = byte

        buffer = [
            82,  # R
            73,  # I
            70,  # F
            70,  # F
            size_list[0],
            size_list[1],
            size_list[2],
            size_list[3],
            87,  # W
            69,  # E
            66,  # B
            80,  # P
            86,  # V
            80,  # P
            56,  # 8
        ]

        for bit in data:
            buffer.append(101 ^ bit)

        return buffer
