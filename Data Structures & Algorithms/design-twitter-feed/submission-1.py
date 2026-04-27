import collections
import heapq

class Twitter:
    def __init__(self):
        self.timer = 0 
        self.followMap = collections.defaultdict(set)
        self.tweetMap = collections.defaultdict(list)        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.timer, tweetId])
        self.timer+=1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        res.extend(self.tweetMap[userId])
        for followeeId in self.followMap[userId]:
            if followeeId != userId: # Don't double-dip!
                res.extend(self.tweetMap[followeeId])
        
        res.sort(key=lambda x: x[0], reverse=True)
        return [tweet[1] for tweet in res[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        