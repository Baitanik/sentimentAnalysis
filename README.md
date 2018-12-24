# sentimentAnalysis
This is very basic program for sentimentAnalysis of twitter feed about some specific keyword.
It will continuously get the live feed from twitter for the specified keyword provided in th argument.
and it print the text and corresponding sentiment (Positive,Negative,Neutral) and their polarity value .

#note : This will get only public tweets, which don't have any restriction imposed by user

#Install the prequisits. 
pip install -r requirements.txt

Get the access token to get the tweets from developer.twitter.com.
Steps to get the access token and keys are mentioned here 
https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html

# Run the program

python sentimentanalysis.py lenovo

# output 
It will first display the text, in the following line sentiment and its polarity value
e.g python sentimentanalysis.py lenovo

b'RT @howtogeek: This is potentially bad news for some Lenovo laptop users in enterprise environments. https://t.co/ZTcDZs1Y4F by @Summerson'
Sentiment : negative , Polarity Value :-0.6999999999999998
b'William Shatner Says #MeToo Movement Not Considering Context - entertainment - Lenovo https://t.co/X2yLgm71RB'
Sentiment : neutral , Polarity Value :0.0






