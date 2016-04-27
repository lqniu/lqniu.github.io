---
layout: post
title: "Greedy Thick Thinning算法"
date:   2015-09-23 09:02:53
categories: research
tags: algorithm
---

#Greedy Thick Thinning

The Greedy Tick Thinning algorithm starts with an empty gtaph and repeatedly adds the arc that
maximally increases the bayesian metric until no arc addition will result in an increase. Then it repeatedly
removes arcs until no arc deletion will result in an increase in the bayesian metric. Thus, the model produced
from this algorithm is the model for which the data is most likely to be observed.The bayesian metric is
computed using equation 3, The bayesian metric for GTT is detailed as follows:

n is the number of variables, ri is the number of states of variable I, Nijk is the number of instance where
variable i takes on states k when its parent is in states j, Nij = sum of Nijk Nijk is the Dirichlet exponent of ,
the probability that variable i is in state k given the parents of i are in state j.




ref:[Structure Learning of Bayesian Networks Using Heuristic Methods](http://ipcsit.com/vol45/047-ICIKM2012-M20002.pdf)
