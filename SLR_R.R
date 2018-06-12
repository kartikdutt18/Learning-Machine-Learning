dataset = read.csv('Salary_Data.csv')
library(caTools)
set.seed(120)
split=sample.split(dataset$Salary,SplitRatio = 0.8)
training_set=subset(dataset,split==TRUE)
test_set=subset(dataset,split==FALSE)
regressor=lm(formula=Salary~YearsExperience,
             data=training_set)
pred=predict(regressor,newdata=test_set)
install.packages('graphics')
library(graphics)
install.packages("ggplot2", dependencies = TRUE)
library(ggplot2)
ggplot()+
  geom_point(aes(x=test_set$YearsExperience,y=test_set$Salary),color='green')+
  geom_line(aes(x=training_set$YearsExperience,y=predict(regressor,newdata=training_set)),color='red')+
  ggtitle('Salary vs Experience')+
  xlab('Years of Experience')+
  ylab('Salary')

    