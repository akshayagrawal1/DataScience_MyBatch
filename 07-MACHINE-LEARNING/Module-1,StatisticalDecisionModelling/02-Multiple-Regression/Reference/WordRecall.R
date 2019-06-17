#
setwd("C:\\Users\\Classroom4\\Desktop\\Day2")

wordRecall <- read.csv("wordRecall.csv")

plot(wordRecall)

#Plot the transformed variables
plot(log(wordRecall$time),wordRecall$prop)

#Fit a linear model

lmRecall <- lm(prop~log(time),wordRecall)
summary(lmRecall)

