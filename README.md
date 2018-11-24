## Sentiment Analysis On News Headlines and Descriptions

#### The news data was obtained from using News api: https://newsapi.org/
#### Pysentiment is a package that contains a financial sentiment dicitionarys. Pysentiment returns  subjectivity and polarity scores for texts. For more information on Pysentiment: https://pypi.org/project/pysentiment/
#### The 100 most liquid stocks can be found here: http://www.wsj.com/mdc/public/page/2_3021-activnyse-actives.html 

 Sentiment Analysis was performed on headlines and descriptions of news articles using Pysentiment on the 9 of most liquid stocks. Any articles without a headline were dropped and descriptions were included if they existed. Polarity and subjectivity scores were added as features in the each stock csv in the data directory.

#### We will analyze the relationships between volume of news, polarity, subjectivity and stock price for JPMorgan Chase and Bank of America.


