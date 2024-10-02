# https://leetcode.com/problems/design-twitter/
from typing import *
from collections import defaultdict

class Twitter:

    def __init__(self):
        
        # twitts by user
        self.twitts:Dict[int,List[int]] = defaultdict(lambda: [])
        # who each user follows
        self.follow_table:Dict[int,Set[int]] = defaultdict(lambda: set())
        self.counter = 0
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twitts[userId].append((self.counter,tweetId))
        self.counter += 1
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        res.extend(self.twitts[userId])
        for followees in self.follow_table[userId]:
            res.extend(self.twitts[followees])
        res.sort(key=lambda it: it[0], reverse=True)
        return [it[1] for it in res[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_table[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_table[followerId]:
            self.follow_table[followerId].remove(followeeId)
        


twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1)  )
twitter.follow(1, 2)   
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1) )
twitter.unfollow(1, 2)  

print(twitter.getNewsFeed(1) )


