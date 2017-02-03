# How Twitter was designed

## Goal of Twitter

People are creating content(tweets) on twitter platform and the jobs are
1. How to send these tweets to all the followers?
2. How to make these Real Time?

## How Twitter solves them

Twitter maintains different types of timelines 
1. User Timeline (All the tweets that a particular user has sent)
2. Home Timeline (Which is a temporal merge of user timelines that a user is following)
3. Query Timeline (Mainly Search API)

#### High level architecture flow

##### Home/User Timelines

1. Tweet comes in, hits the right server
2. Fanout demon queries social graph service(Flock - which holds all the followers and followings of people)
3. Iterates through all the followers timelines stored in redis cluster(which has replication factor of 3) and add this tweet id, user id and some other information to all the home timelines
4. Size of home timeline in per user in Redis cluster is 800
5. This home timeline will also be stored in disc also for persistent storage
6. User timeline will always be stored in disk, because fetching user timeline is not latency intensive as it will be a single query
7. As one can clearly see reads are extremely faster when compared to writes (Since Read-Write ratio of request rate will be > 50)

##### Query Timeline

1. When Tweet comes in, twitter is going to tokenize and ingest into an earlybird machine (Modified version of Lucene), Entire Lucene index is stored in RAM
2. Blender (Which creates search timeline in Twitter) issues a search query to early bird cluster, which internally queries every shard of earlybird
3. Ranking is mainly done through number of re-tweets and favorites
4. These re-tweets/favorites are calculated in activity timeline when user re-tweets/favorites
5. So Blender will get tweet ids from earlybird and it recomputes and sorts(based on ranking) the results

#### Problems in Home timeline

1. When the user who has Millions of followers, If that user tweets twitter is going to store those tweet id in each and every follower home timeline which might be computationally expensive
2. Solution for it is twitter is going to store tweet ids in home timelines of users if number of followers are less then some threshold, And while fetching twitter will do temporal merge of tweet ids with user timeline who has more number of followers, This way reads become slow (Tradeoff) (Experimental Phase)

#### Where the actual tweet is stored

1. It is stored in Tweetie-Pie service
2. From home timeline we will get tweet ids and do a batch get on tweetie-pie service

## Credits

1. [Design Twitter](https://www.youtube.com/watch?v=gX8S7b8UYl8)