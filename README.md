TwitterTrending
===============
 Assignment question:
 
 In this assignment, you would learn how to analyze big data using Hadoop. Specifically, you would collect Twitter data and analyze to determine a trend in a topic of your choice. Here are the intermediate steps:

 

Collect Twitter data using Twitter API - collect about 100-200MB data
Pick a topic of your interest. For example, News, Sports, Fashion, Christman Shopping/Gifts, Politics, Finance etc. You need to write an analytics to detect "what is trending?" in twitter data. I have provided a simple algorithm that is similar to word counting with some modifications. It is also okay to detect general "what is trending" without any topic of interest.
Next I want you to implement a Hadoop/Map Reduce version of your algorithm. One example algorithm for trending is as follows: You only count meaningful words and ignore general/common words like this, that, here, a, there, home etc. Now you would rank the meaningful words based on their frequency. Once you rank those, then you could simply list those as trends or do some more trick. You go back to searching those twits where these words have occured and try to pull some news or set of associated words that occur with these high frequency words.
Next you create an EMR. Copy your twit data to a S3 bucket. Run your algorithm there and show the results.
I may provide you access to a S3 bucket with 10GB data to run against real big data. But before that, you need to complete 1-4 to ensure it is all working correctly.
To understand and visualize trend, it is sometimes useful to create a figure like the one I have attached here. See if you can generate such a diagram to understand your twits. That would be cool. You get 20 points extra for this. Also 20 points extra for meaningful trend detection.
