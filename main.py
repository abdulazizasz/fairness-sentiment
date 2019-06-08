import helper 
import sentiment
import pandas as pd 


def mine(x):
    return len(x)

if __name__ == "__main__":
    pd.options.mode.chained_assignment = None 
    sentiments_api = ['TextBlob_Sentiment','Vader_Sentiment','NLTK_Setiment','MonkeyLearn_Sentiment']
    df = helper.prepare_data()
    df.columns = ['sentence']
    
    sample_df = df

    # sample_df[sentiments_api[0]] = sample_df['sentence'].apply(sentiment.TextBlob_Sentiment)
    sample_df[sentiments_api[1]] = sample_df['sentence'].apply(sentiment.Vader_Sentiment)
    # sample_df[sentiments_api[2]] = sample_df['sentence'].apply(sentiment.NLTK_Setiment)
    sample_df[sentiments_api[3]] = sample_df['sentence'].apply(sentiment.MonkeyLearn_Sentiment)
    print(sample_df)