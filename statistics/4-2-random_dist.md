[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>>Here's the code  
import numpy as np  
test = np.random.random(1000)
pmf = thinkstats.Pmf(test)  
thinkplot.Pmf(pmf)  
thinkplot.show(xlabel='random', ylabel='pmf')
>> This creates a graph that shows that there are now many numbers generated at random  
cdf = thinkstats.Cdf(test)  
thinkplot.Cdf(cdf)  
thinkplot.show(xlabel='random', ylabel='cdf')  
>> This creates a distribution graph that shows a relatively uniform distribution trend indicating the random number generation works out quite gradually   
