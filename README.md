# MangaRock-dl
Simple script for downloading mangas from mangarock.com in webp, png, or jpg.
Python required (Tested in Python3.6).
# INSTALLATION
You must first clone/download the project to your computer.
## Required Python Packages
These are required python modules for the script to work.
- requests [requests](https://pypi.org/project/requests/)
## Additional Extensions
The default downloaded file is webp (recommended). For conversion to png and jpg, the following 3rd party module is required.
- webP [webP](https://developers.google.com/speed/webp/download)

Download webP and link the `/bin` folder inside to your `PATH`.
# RUN SCRIPT
To start downloading, go to and find the `OID` of your selected manga in the url.
- For example, the oid of `https://mangarock.com/manga/mrs-serie-358279` would be `358279`.

To check the available chapters, run:
`python3 Main.py -s {OID} -i`
Take note of the chapter index you want to donwload (ignore this if you want to download the entire manga). Note that this does not download anything.

To download the chapters, run:
`python3 Main.py -s {OID}`

## Optinal Arguments
- `-r / --range` specifies the range of chapters you want to download. Default is all. For example `1,3,5,6-20,35`
- `-d / --directory` specifies the directory which the manga will be downloaded. Default is current directory. For example `mangaHome/`
- `-f / --format` specifies the format of the downloaded file. Default is `webp`. Can pass in `jpg` or `png` as argument, but make sure additional extension is installed.
