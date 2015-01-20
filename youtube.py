import gdata.youtube
import gdata.youtube.service
import os
import time

yt_service = gdata.youtube.service.YouTubeService()
yt_service.ssl = True

yt_service.developer_key = ''

urllst=[]


def main():
	with open('list.txt') as fl:
		for line in fl:
			line = line.strip()
			SearchVid(line)


def SearchVid(search_terms):
	query = gdata.youtube.service.YouTubeVideoQuery()
	query.vq = search_terms
	query.orderby = 'viewCount'
	query.racy = 'include'
	query.max_results = 1
	feed = yt_service.YouTubeQuery(query)
	for entry in feed.entry:
		print entry.media.title.text
		dwlVid(entry.media.player.url)

def dwlVid(vid):
	os.system("youtube-dl --extract-audio --audio-format mp3 -l %s"%vid)
	time.sleep(10)


main()


