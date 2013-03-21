install.packages('tm')
install.packages('RWeka')
source("http://bioconductor.org/biocLite.R")
biocLite("Rgraphviz") 
readvanilla <- function (elem, language, id) 
{
  
  doc <- PlainTextDocument(elem$content, id = id, language = language)
}


tweets <- read.csv('tweets_Galaxy S III_05_00_54.csv')

# Read just the tweet text into the corpus
corpus <- Corpus(VectorSource(tweets$text),readerControl=list(reader = readvanilla))
Sys.setlocale("LC_COLLATE", "C")

# Make our document-term matrix
dtm <- DocumentTermMatrix(corpus, control = list(stemming = FALSE,
                                                                                                stopwords = TRUE, 
                                                 minWordLength = 3,
                                                 removeNumbers = TRUE, 
                                                 removePunctuation = TRUE))
findAssocs(dtm,term="galaxy",0.2)
plot(dtm, terms = names(findAssocs(dtm,term="galaxy",0.2)), corThreshold = 0.30)