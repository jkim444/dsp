[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Here's the code  
import thinkstats2  
import nsfg  
import thinkplot  

resp = nsfg.ReadFemResp()  
pmf = thinkstats2.Pmf(resp.numdkhh, label='numdkhh')  
biased_pmf = BiasPmf(pmf, label='biased')  

thinkplot.preplot(2)  
thinkplot.Pmfs([pmf, biased_pmf])  
thinkplot.show(xlabel='number of children', ylabel='pmf')

>> This would create distribution graph with two groups with different trend  

print(pmf.Mean())  
print(biased_pmf.Mean())

>> This would compare two means as 1.024.. vs 2.403..  
