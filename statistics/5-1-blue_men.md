[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> Here is the code  
  
import scipy.stats  
  
test = scipy.stats.norm(loc=178, scale=7.7)  
  
>> Calculating the percentage of people of one standard deviation below the mean is as below . 
  
print test.cdf(178 - 7.7)  
// This yields 0.158... approximately 16%  
  
>> Now, to calculate the portion of people between 5'10" (177.8cm) and 6'1"(185.4cm), we can get the percentage between two values in the distribution as below.  
  
print test.cdf(185.4) - test.cdf(177.8)  
// This yields 0.342... approximately 34%  

