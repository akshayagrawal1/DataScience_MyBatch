setwd("C:\\Users\\Classroom4\\Desktop\\Day2")

# MULTIPLE LINEAR REGRESSION MODEL BUILDING

# Read in World Crude Oil Output data
CrudeOilOutput <- read.csv("CrudeOilOutput.csv", header = T, sep = ",")
CrudeOilOutput

# Check for correlations
correlation <- cor(CrudeOilOutput)
correlation
plot(CrudeOilOutput)

CrudeOilOutputlm <- lm(CrudeOilOutput$WorldOil ~ CrudeOilOutput$USEnergy
                       + CrudeOilOutput$USAutoFuelRate
                       + CrudeOilOutput$USNuclear + CrudeOilOutput$USCoal
                       + CrudeOilOutput$USDryGas, CrudeOilOutput)
summary(CrudeOilOutputlm)
par(mfrow=c(2,2))
plot(CrudeOilOutputlm)

# Load required libraries
library(MASS)
library(car)

# Use stepAIC to build model based on AIC
stepAIC(CrudeOilOutputlm, direction = "both")



# MTcars example
head(mtcars)

mtcarsLmOut <- lm(mpg~. , data=mtcars)
summary(mtcarsLmOut)


vif(mtcarsLmOut)
mtcarsStepOut <- stepAIC(mtcarsLmOut)

vif(mtcarsStepOut)
