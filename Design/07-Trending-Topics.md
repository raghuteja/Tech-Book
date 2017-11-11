# Design Trending Topics

### Identifying trending topics

If a term has a huge volume compared to the past, the term should be identified as popular

**Why should we compare with past data?**

There might be some common terms which will be used very frequently all the time, we should not consider them as trending topics. To avoid them we should compare with past data

**What happens if a new topic occurs 100 times which has not occurred in past?**

If we consider the ratio of current occurrence count and past, this term will come up to trending which is not what we are expecting

We need to dilute such small occurrences that occurred very few times in past

(volume last few hours) / (volume within last X days + 10000)

### Credits

1. [Gainlo](http://blog.gainlo.co/index.php/2016/05/03/how-to-design-a-trending-algorithm-for-twitter/)
