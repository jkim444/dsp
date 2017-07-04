[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> REPLACE THIS TEXT WITH YOUR RESPONSE . 
def CohenEffectSize(g1, g2):  
  diff = g1.mean() - g2.mean() . 
  var1 = g1.var() . 
  var2 = g2.var() . 
  n1, n2 = len(g1), len(g2) . 
  pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2) . 
  d = diff / math.sqrt(pooled_var) . 
  return d . 

CohenEffectSize(firsts.prglngth, others.prglngth) . 
# = 0.028879044654449883 . 
  
CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb) . 
# = -0.088672927072602 . 

>> It explains earlier that 0.029 is quite small effect size for the pregnancy length.  
>> The Cohen's d value for the total weight is quite small as well and negative number.  
>> I assume that means that the difference on the matter between two groups is not so large and not-first-babies are heavier having that I set the 'others' group as group2 in the code.
