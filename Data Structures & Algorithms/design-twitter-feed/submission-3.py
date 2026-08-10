class Twitter:

    def __init__(self):
        self.tweet_table = defaultdict(list)
        self.follow_table = defaultdict(set)
        self.counter = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter+=1
        self.tweet_table[userId].append((self.counter, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow_table[userId].add(userId)
        heap = [] # max_heap
        out = []
        for otherUserId in self.follow_table[userId]:
            postArr = self.tweet_table[otherUserId]
            if postArr:
                idx=len(postArr)-1
                last_post = postArr[idx]
                ct, t_id = last_post
                heapq.heappush(heap, (-ct, t_id, otherUserId, idx))

        count = 10
        while heap and count > 0:
            _, t_id, otherUserId, idx = heapq.heappop(heap)
            out.append(t_id)
            if idx > 0:
                next_post = self.tweet_table[otherUserId][idx-1]
                ct, n_t_id = next_post
                heapq.heappush(heap, (-ct, n_t_id, otherUserId, idx-1))
            count -= 1
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_table[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.follow_table[followerId]:
            self.follow_table[followerId].remove(followeeId)
