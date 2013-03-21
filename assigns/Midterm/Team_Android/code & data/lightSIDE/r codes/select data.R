####Slectingdata by source###
all <- read.csv(file= "/Users/YueHan/Desktop/alltweets.csv", header=TRUE)
attach(all)
all

android<-subset(all,source_cleaned=="Android")
android
write.csv(android, file = "/Users/YueHan/Desktop/androidall.csv")

iOS<-subset(all,source_cleaned=="iOS")
iOS
write.csv(iOS, file = "/Users/YueHan/Desktop/iOSall.csv")

BlackBerry<-subset(all,source_cleaned=="BlackBerry")
BlackBerry
write.csv(BlackBerry, file = "/Users/YueHan/Desktop/BlackBerryall.csv")

WindowsPhone<-subset(all,source_cleaned=="WindowsPhone")
WindowsPhone
write.csv(WindowsPhone, file = "/Users/YueHan/Desktop/WindowsPhoneall.csv")