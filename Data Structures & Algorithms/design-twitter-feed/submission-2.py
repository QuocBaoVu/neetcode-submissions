class Twitter:

    def __init__(self):
        self.tweet_table = defaultdict(list)
        self.follow_table = defaultdict(set)
        self.counter = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow_table[userId].add(userId)
        self.counter+=1
        self.tweet_table[userId].append((self.counter, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [] # max 10 post
        for otherUserId in self.follow_table[userId]:
            postArr = self.tweet_table[otherUserId]
            for post in postArr:
                heapq.heappush(heap, post)
                if len(heap) > 10:
                    heapq.heappop(heap)
        heap.sort(reverse=True)
        out = [i[1] for i in heap]
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_table[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.follow_table[followerId]:
            self.follow_table[followerId].remove(followeeId)
