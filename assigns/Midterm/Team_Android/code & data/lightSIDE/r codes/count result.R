###Counting result######

###android###
android <- read.csv(file= "/Users/YueHan/Desktop/androidresult.csv", header=TRUE)
attach(android)
android

ant<-table(topic, class)
write.csv(ant, file = "/Users/YueHan/Desktop/ant.csv")

###blackberry###
bb <- read.csv(file= "/Users/YueHan/Desktop/bbresult.csv", header=TRUE)
attach(bb)
bb

bbt<-table(topic, class)
write.csv(bbt, file = "/Users/YueHan/Desktop/bbt.csv")

###ios####
ios <- read.csv(file= "/Users/YueHan/Desktop/iosresult.csv", header=TRUE)
attach(ios)
ios

iost<-table(topic, class)
write.csv(iost, file = "/Users/YueHan/Desktop/iost.csv")

###windows####
windows <- read.csv(file= "/Users/YueHan/Desktop/windowscal.csv", header=TRUE)
attach(windows)
windows

table(tweettopic, class)

bbios <- read.csv(file= "/Users/YueHan/Desktop/bbios_bbresult.csv", header=TRUE)
attach(bbios)

bbiost<-table(topic, class)
write.csv(bbiost, file = "/Users/YueHan/Desktop/bbiost.csv")
