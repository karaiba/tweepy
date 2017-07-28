#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = 240814375-S5Us4PODFQV73GJAYlt3neMK2e5K0UQ6aFItrn9T
access_token_secret = Mj20HMHxNkwTVK6wYL4z8kKfDITOeK0fnnDUGC1BAAZYq
consumer_key = 8USNprCJgfw7zgCBsoM1twTZ1
consumer_secret = M5fWOB7iJojKLuQT5y7yENOwj0kD0xwyECR3AO5x7OkrhsFoPJ


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
