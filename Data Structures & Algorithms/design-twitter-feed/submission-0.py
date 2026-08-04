class Twitter:

    def __init__(self):
        self.followLists = {}
        self.tweets = []
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        following = self.followLists.get(userId, [])
        tweetStack = list(self.tweets)
        print(tweetStack)
        while len(posts) < 10 and tweetStack:
            tweet = tweetStack.pop()
            if tweet[0] == userId or tweet[0] in following:
                posts.append(tweet[1])
        return posts
        

    def follow(self, followerId: int, followeeId: int) -> None:
        followList = self.followLists.get(followerId)
        if followList and followeeId not in followList:
            self.followLists[followerId] = followList.append(followeeId)
        elif not followList:
            self.followLists[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followList = self.followLists.get(followerId)
        if followList and followeeId in followList:
            self.followLists[followerId] = [id for id in followList if id != followeeId]

