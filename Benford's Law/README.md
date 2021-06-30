----------------------------------------------------------------------------------------------------------------------------------------------------------------------
The Benford’s law:

According to Benford’s law, also known as the first-digit law, the frequency of occurrence of the leading digits in naturally occurring numerical distributions
is predictable and nonuniform. In fact, a given number is six times more likely to start with a 1 than a 9! This is very counterintuitive, as most
people would expect a uniform distribution, with each number having a one in nine (11.1 percent) chance of occupying the first slot. Due to this cognitive
disconnect, Benford’s law has become a useful tool for fraud detection in financial, scientific, and election data.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

The aim of this exercise is to write a program that loads numerical data, records the frequency of occurrence of the first digits, compares these to Benford’s law 
using the chi-square goodness-of-fit test, and presents the comparison in both tabular and graphical form.

For this project, a dataset of voting records from the 2016 US presidential election is used. This consists of the final by-county votes for the
102 counties in the state of Illinois, which was won by Hillary Clinton. The final result is then a comparison between the real presidential election data and the Benford's law.

The script "beat_benford_practice.py" manipulates the vote counts so the final result conforms to the Benford's law. 
The script "benford.py" checks, with a chi-square test, the conformance of the Benford's law ploting the real data and the theorical Benford data. 

Modules used: sys, math, collections, matplotlib.pyplot
