#import the dataset in a csv format
twtest <- read.csv(file= "/Users/Harris/Dropbox/STEVENS/D Semester/Winter/tweets02_28.csv", fileEncoding = "UTF-8", sep = ",")
#get a summary of the imported dataset
summary(twtest)
class(twtest)

################################################################################################################################################################
#
#
#
#           DECREASE THE NUMBER OF SOURCES IN ORDER TO BE ANALYZED
#
#
################################################################################################################################################################
# get the source of the tweets
twtest$source[1:10]
#convert the source to a character string
twtest$source<- as.character(twtest$source)
class(twtest$source)

################################################################################################################################################################
#Android
androidsource <- c()
kw <- c("Android","Falcon Pro","twicca","  HTC Peep","FalconPro","ZOOKEEPER BATTLE","LazyUnfollow - Droid","Gone Fishing mobile game","SwiftKey personalization")
for (i in seq(1, length(kw))){
  androidsource <- c(androidsource, grep(kw[i], twtest$source,ignore.case = TRUE))
}
#get only the unique values in the list
androidsource <- unique(androidsource)
length(androidsource)
twtest$source[androidsource][1:100]

################################################################################################################################################################
#iPhone
iphonesource <- c()
kw <- c("iPhone", "iOS", "iPad","Sylfeed", "TweetList!","Zite Personalized Magazine","iHoroscope")
for (i in seq(1, length(kw))){
  iphonesource <- c(iphonesource, grep(kw[i], twtest$source,ignore.case = TRUE))
}
#get only the unique values in the list
iphonesource <- unique(iphonesource)
length(iphonesource)
twtest$source[iphonesource][1:100]
################################################################################################################################################################

# blackberry
# find all positions of sources that contain Blackberry as source
bbsource <- c()
kw <- c("Texas Hold'em King LIVE","QuickPull","Blackberry")
for (i in seq(1, length(kw))){
  bbsource <- c(bbsource, grep(kw[i], twtest$source,ignore.case = TRUE))
}
#get only the unique values in the list
bbsource <- unique(bbsource)
length(bbsource)
twtest$source[bbsource][1:100]

################################################################################################################################################################
#windows phone
wnphone <- c()
kw <- c("Windows Phone", "rowi for Windows Phone","winph0","Social by Nokia")
for (i in seq(1, length(kw))){
  wnphone <- c(wnphone, grep(kw[i], twtest$source,ignore.case = TRUE))
}
#get only the unique values in the list
wnphone <- unique(wnphone)
length(wnphone)
twtest$source[wnphone]

################################################################################################################################################################
#mobile-not identified
#mobile_ufo
mobufosource <- c()
kw <- c( "Janetter", "Write Longer", "Neatly BB10", "PicsArt Photo Studio","UnfolllowID","GREE","RuleKingdom","Airport City Mobile", "runtastic", 
         "Echofon","Truecaller","Scoop.it","Pulse News", "Mobile Web (M2)" , "Mobile Web (M5)" ,"Flipboard", "Instagram", "Viber")
for (i in seq(1, length(kw))){
  mobufosource <- c(mobufosource, grep(kw[i], twtest$source,ignore.case = TRUE))
}
#get only the unique values in the list
mobufosource <- unique(mobufosource)
length(mobufosource)
twtest$source[mobufosource][1:100]

################################################################################################################################################################
#web
websource1 <- c()
kw <- c("Google", "twitterfeed", "Tweet Button", "Hotot for Chrome", "TweetDeck", "Facebook","Tweet Old Post","WordPress.com","WP Twítter","NetworkedBlogs","Megamobilecontent")
for (i in seq(1, length(kw))){
  websource1 <- c(websource1, grep(kw[i], twtest$source,ignore.case = TRUE))
}
#get the plain web ones
websource2 <- grep("web", twtest$source, fixed = TRUE)
#get only the unique values in the list
websource <- unique(c(websource1,websource2))
length(websource)
################################################################################################################################################################
#mac
macsource <- c()
kw <- c("Tweetbot for Mac","YoruFukurou", "Twееtbot for Mac","Twitter for Mac", "OS X" )
for (i in seq(1, length(kw))){
  macsource <- c(macsource, grep(kw[i], twtest$source,ignore.case = TRUE))
}
#get only the unique values in the list
macsource <- unique(macsource)
length(macsource)
################################################################################################################################################################
#Windows Desktop
wndesk <- c()
kw <- c("Tween","Windows Live Writer")
for (i in seq(1, length(kw))){
  wndesk <- c(wndesk, grep(kw[i], twtest$source,ignore.case = TRUE))
}
#get only the unique values in the list
wndesk <- unique(wndesk)
twtest$source[wndesk]
length(wndesk)
################################################################################################################################################################
#Business Suites
bussource <- c()
kw <- c("Buffer" ,"HootSuite","IFTTT" ,"Scope App","WPTweetily","dlvr.it","Spread The Next Web","Thirst for Topics",
        "SocialEngage","SocialOomph","SharedBy", "MarketMeSuite","Sprout Social","SNS Analytics","GroupTweet")
for (i in seq(1, length(kw))){
  bussource <- c(bussource, grep(kw[i], twtest$source,ignore.case = TRUE))
}
#get only the unique values in the list
bussource <- unique(bussource)
length(bussource)
################################################################################################################################################################
#ufos
# no idea what they are and personalized sources
ufos <- c()
kw <- c("hisobot","txt","Gravity!","multibt","GamerNews","AboutDiablo.com",
        "Water Filters Cartridges Site","byodrt","socnet2socnet","imbetjoy","Twit Posts RU","Rewwwind","FileDir.com", "LinkedIn")
for (i in seq(1, length(kw))){
  ufos <- c(ufos, grep(kw[i], twtest$source,ignore.case = TRUE))
}
#get only the unique values in the list
ufos <- unique(ufos)
length(ufos)

#UFOS
# no idea what they are
#    "hisobot","txt","Gravity!"
#personalized
#    "multibt","GamerNews","AboutDiablo.com","Water Filters Cartridges Site","byodrt","socnet2socnet","imbetjoy","Twit Posts RU","Rewwwind","FileDir.com"

################################################################################################################################################################
#JAPAN
japansource <- c()
kw <- c("WIWA SERVICE","Sylfeed","rakubo2","OpenTween","twittbot.net","EasyBotter","bot_manager","upmeetup","YoruFukurou")
for (i in seq(1, length(kw))){
  japansource <- c(japansource, grep(kw[i], twtest$source,ignore.case = TRUE))
}
#get only the unique values in the list
japansource <- unique(japansource)
length(japansource)
################################################################################################################################################################

  
source_cleaned <- c()
 for (i in seq(1, length(twtest$source))){
   if (is.element(i, androidsource)){
     source_cleaned <- c(source_cleaned, "Android")
   }else if (is.element(i, iphonesource)){
     source_cleaned <- c(source_cleaned, "iOS")
   }else if (is.element(i, bbsource)){
     source_cleaned <- c(source_cleaned, "BlackBerry")
   }else if (is.element(i, wnphone)){
     source_cleaned <- c(source_cleaned, "WindowsPhone")
   }else if (is.element(i, mobufosource)){
     source_cleaned <- c(source_cleaned, "MobileUFO")
   }else if (is.element(i, websource)){
     source_cleaned <- c(source_cleaned, "Web")
   }else if (is.element(i, macsource)){
     source_cleaned <- c(source_cleaned, "Mac")
   }else if (is.element(i, wndesk)){
     source_cleaned <- c(source_cleaned, "WindowsDesktop")
   }else if (is.element(i, bussource)){
     source_cleaned <- c(source_cleaned, "BusinessSuite")
   }else if (is.element(i, ufos)){
     source_cleaned <- c(source_cleaned, "Personalized")
   }else if (is.element(i, websource)){
     source_cleaned <- c(source_cleaned, "Web")
   }else if (is.element(i, japansource)){
     source_cleaned <- c(source_cleaned, "JapanWebsite")
   }else{
     source_cleaned <- c(source_cleaned, "NotIdentified")
   }
 }

  ## check if all went well
  source_cleaned[1:40]
  class(source_cleaned)
  
  
  #change all of the columns from factors to character or number variables
  class(twtest$user)
  twtest$user <- as.character(twtest$user)
  #
  # twtest$date
  #
  twtest$source <- as.character(twtest$source)
  twtest$retweets <- as.integer(twtest$retweets)
  twtest$tweet <- as.character(twtest$tweet)
  twtest$followers <- as.integer(twtest$followers)
  twtest$statuses <- as.integer(twtest$statuses)
  twtest$listed <- as.integer(twtest$listed)
  twtest$friends <- as.integer(twtest$friends)

# Add a Source_Cleaned column
twtest<- cbind(twtest,source_cleaned)
#how many unidentified
  length(twtest$source[twtest$source_cleaned =="NotIdentified"])
  
#find the source of the "NotIdentified"
  sort(twtest$source[twtest$source_cleaned =="NotIdentified"], decreasing=FALSE)
  
  
  ################################################################################################################################################################
  #
  #
  #
  #           TWEET TOPIC - ADD A COLUMN WITH WHAT THE TWEET IS ABOUT 
  #
  #
  ################################################################################################################################################################

  #Firefox OS
  kwios <- c(grep("iOS", twtest$tweet,ignore.case = TRUE), grep("iPhone", twtest$tweet,ignore.case = TRUE))
  length(kwios)
  kwandroid <- c(grep('Android', twtest$tweet,ignore.case = TRUE), grep('Android OS', twtest$tweet,ignore.case = TRUE))
  kwblackberry <- c(grep('Blackberry', twtest$tweet,ignore.case = TRUE), grep('Blackberry OS', twtest$tweet,ignore.case = TRUE))
  kwwinphone <- c(grep('Windows Phone OS', twtest$tweet,ignore.case = TRUE),grep('Windows Phone', twtest$tweet,ignore.case = TRUE))

  # check how many tweets have been classified
  length(kwios) +   length(kwandroid) +   length(kwblackberry) +   length(kwwinphone) #12928
  #number of total tweets is less 
  length(twtest$user) #12678
  
  # create special cases for tweets with multiple mentions
  # interference of two
  android_ios <- intersect(kwios,kwandroid)
  android_bb <- intersect(kwandroid, kwblackberry)
  ios_bb <-   intersect(kwios,kwblackberry) 
  android_winphone <- intersect(kwandroid, kwwinphone) 
  ios_winphone <-   intersect(kwios,kwwinphone)
  bb_winphone <-   intersect(kwblackberry,kwwinphone) 
  
  length(android_ios)
  length(android_bb)
  length(ios_bb)
  
  #sets of three
  android_ios_bb <- intersect(android_ios,kwblackberry)
  android_ios_winphone <- intersect(android_ios, kwwinphone)
  android_bb_winphone <- intersect(android_bb, kwwinphone)
  ios_bb_winphone <- intersect(ios_bb, kwwinphone)
  
  #set of all 4 mobile OS
  all4 <- intersect(android_ios,bb_winphone)
  
  
  # create an empty list to put the topics!
  tweettopic <- rep("NoTweetKeywords", length(twtest$tweet))
  #one
  tweettopic[kwios] <- "iOS"
  tweettopic[kwblackberry] <- "Blackberry"
  tweettopic[kwwinphone] <- "WindowsPhone"
  tweettopic[kwandroid] <- "Android"
  #two
  tweettopic[android_ios] <- "Android_iOS"
  tweettopic[android_winphone] <- "Android_WindowsPhone"
  tweettopic[android_bb] <- "Android_BB"
  tweettopic[ios_winphone] <- "iOS_WindowsPhone"
  tweettopic[bb_winphone] <- "BB_WindowsPhone"
  tweettopic[ios_bb] <- "iOS_BB"
  #three
  tweettopic[android_ios_bb] <- "Android_iOS_BB"
  tweettopic[android_ios_winphone] <- "Android_iOS_WindowsPhone"
  tweettopic[android_bb_winphone] <- "Android_BB_WindowsPhone"
  tweettopic[ios_bb_winphone] <- "iOS_BB_WindowsPhone"
  # all 4 topics
  tweettopic[all4] <- "AllOperatingSystems"
  

  #confirm that unclassified tweets are indeed unrelated
  twtest$tweet[tweettopic == "NoTweetKeywords"][1:100]
  
  
  # Add a Topic of the Tweet Column
  length(tweettopic)
  twtest<- cbind(twtest,tweettopic)
  
  # find how many of the tweets did not have any of the keywords
  length(twtest$tweet[twtest$tweettopic == "NoTweetKeywords"])

  # delete the tweets that did not contain any of the keywords
  twtest2 <- subset(twtest, tweettopic!="NoTweetKeywords")
  length(twtest2$user)  
  length(twtest$user)
  twtest <- twtest2
  rm(twtest2)
  
# Write to a file, with row names
write.csv(twtest, "tweets_source_and_topic.csv", row.names=TRUE)

################################################################################################################################################################
#
#
#
#           POSITION OF TWEETS FOR EACH OF THE CATEGORIES
#
#
################################################################################

#1. MOBILE VS. DESKTOP
#MOBILE ALL
c(androidsource,iphonesource,bbsource, wnphone, mobufosource)
#DESKTOP ALL
c(websource, macsource, wndesk, bussource
  ###############################################################################
  #2. ANDROID VS. IOS USERS VS. WINDOWS PHONE VS. BLACKBERRY
  #ANDROID USERS
  androidsource
  #ios users
  iphonesource
  # win phone users
  wnphone
  # blackberry
  bbsource
  ###############################################################################
  # 3. GOOGLE VS. APPLE USERS
  # ANDROID AND CHROME USERS
  c(androidsource, grep("Chrome", twtest$source,ignore.case = TRUE))
  # APPLE USERS
  c(iphonesource, macsource)
  ###############################################################################
  # 4. UNIDENTIFIED (COMPARE WITH THEMSELVES :p)
  c(ufos, JAPAN)
  ###############################################################################
  
  ####directory#########################################
  #Android --- androidsource
  #iPhone ---- iphonesource
  # blackberry ---bbsource
  #windows phone --- wnphone
  #mobile not identified --- mobufosource 
  ###########################################33
  # desktop all
  #web --- websource
  #mac ---- macsource
  #Windows Desktop ---- wndesk
  #Business Suites --- bussource
  ########################################
  #unidentified
  #ufos --- ufos
  #JAPAN --- japansource
  ########################################  

  ##############
  grepl returns a logical vector. You can use the ! operator if you want the opposite result.
  data$ID[!grepl("xyx", data$ID) & data$age>60]
  ################
  
  
  # Write to a file, with row names
  #write.csv(twtest, "tweets_clean_source.csv", row.names=TRUE)
  
  

