import instaloader

def get_user_info(username):
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        
        posts = list(profile.get_posts())
        
        hashtags = []
        for post in posts:
            description = post.caption
            if description:
                words = description.split()
                for word in words:
                    if word.startswith("#"):
                        hashtags.append(word)
        
        total_likes = 0
        total_comments = 0
        for post in posts:
            total_likes += post.likes
            if post.comments:
                total_comments += post.comments

        interaction_stats = {
            "likes_received": total_likes,
            "comments_received": total_comments,
            "total_likes": total_likes,
            "total_comments": total_comments
        }
        
        top_posts = [{
            "url": post.url,
            "likes": post.likes,
            "comments": post.comments
        } for post in posts[:5]]
        
        recent_posts = [{
            "url": post.url,
            "image_url": post.url,
            "description": post.caption,
            "likes": post.likes,
            "comments": post.comments
        } for post in posts[:5]]
        
        top_locations = []
        for post in posts:
            location = post.location
            if location:
                top_locations.append(location.name)
        
        current_location = profile.external_url
        
        phone_number = getattr(profile, 'phone_number', None)
        
        user_info = {
            "username": profile.username,
            "full_name": profile.full_name,
            "biography": profile.biography,
            "profile_pic_url": profile.profile_pic_url,
            "followers": profile.followers,
            "following": profile.followees,
            "posts": len(posts),
            "interaction_stats": interaction_stats,
            "top_posts": top_posts,
            "recent_posts": recent_posts,
            "top_hashtags": hashtags[:5],
            "top_locations": list(set(top_locations))[:5], 
            "current_location": current_location,
            "phone_number": phone_number, 
            "website": profile.external_url
        }
        
        return user_info
    except Exception as e:
        return {"error": str(e)}
