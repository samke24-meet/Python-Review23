def create_youtube_video(title,description) :
	video = { "title" : title , "description" : description , "likes" : 0 , "comments" : {} }
	return video

def like(video) :
	if "likes" in video :
		video["likes"] = video["likes"] + 1 
	return video

def dislike(video) :
	if "dislikes" in video :
		video["dislikes"] += 1
	return video

def add_comment( youtubevideo , username , comment_text ) :
	youtubevideo["comments"][username] = comment_text
	return youtubevideo

n = create_youtube_video("DINOSAUR","DINOSAUR EATING CAKE")
print(n)
like(n)
n["dislikes"] = 0
dislike(n)
add_comment( n , "hadeel" , "I like tiramisu")
print(n)
n["likes"] = n["likes"]+495
print(n["likes"])

