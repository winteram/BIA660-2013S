import gdata.youtube
import gdata.youtube.service
import urlparse

yt_service = gdata.youtube.service.YouTubeService()
yt_service.developer_key = 'AI39si7_kNGXrLOTPppUbOn2357HxYWvegR0lBaBdsTct389t6Bew0tEesZcV66tFPK7UgS1vrgfKn2gL_WWuFKWMe6xFGVJ2A'
yt_service.client_id = 'lzhang20@stevens.edu'

def WriteCommentFeed(video_id):
	comment_feed_url = "http://gdata.youtube.com/feeds/api/videos/%s/comments"
	url = comment_feed_url % video_id
	comment_feed = yt_service.GetYouTubeVideoCommentFeed(uri=url)
	counter = 0
	try:
		while comment_feed:
			for comment_entry in comment_feed.entry:
				f = open('comment_Lenovo_top100.xml', 'a')
				print >> f, comment_entry
				# print comment_entry.author[0].name.text
				# print comment_entry.title.text
				# print comment_entry.published.text
				# print comment_entry.updated.text
				# print comment_entry.content.text
				counter = counter + 1
			comment_feed = yt_service.Query(comment_feed.GetNextLink().href) 
	except:
			pass
	return counter

def PrintEntryDetails(entry):
	entry_file = open('video_Lenovo_top100.xml','a')
	print >> entry_file, entry
	# print 'Video title: %s' % entry.media.title.text
	# print 'Video watch page: %s' % entry.media.player.url
	# print 'Video published on: %s ' % entry.published.text
	# print 'Video view count: %s' % entry.statistics.view_count
	# print 'Video rating: %s' % entry.rating.average
	# print 'Video raters amount: %s' % entry.rating.num_raters
	uri2 = entry.media.player.url
	url_data = urlparse.urlparse(uri2)
	query2 = urlparse.parse_qs(url_data.query)
	video_id = query2["v"][0]
	# print video_id
	num = WriteCommentFeed(video_id)
	print 'Comment amount: %s' % num
	print '--------------------------------------------------------------'

def PrintVideoFeed(feed):
	for entry in feed.entry:
		PrintEntryDetails(entry)

def SearchAndPrint(search_terms):
	yt_service = gdata.youtube.service.YouTubeService()
	query = gdata.youtube.service.YouTubeVideoQuery()
	query.vq = search_terms
	query.orderby = 'viewCount'
	query.racy = 'include'
	query.time = 'all_time'
	# Dell: dellvlog; HP: hpcomputers; Apple: Apple; lenovo: LenovoVision
	query.author = 'hpcomputers'
	query.max_results = 50
	query.start_index = 1
	feed = yt_service.YouTubeQuery(query)
	PrintVideoFeed(feed)


def main():
	SearchAndPrint('HP')
	


if __name__ == "__main__":
	main()
