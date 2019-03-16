/************************************************************************
*Name: Aadish Joshi
*Email: asj170430@utdallas.edu
*Number of problems solved: 4
************************************************************************/


Problem 2:

Programming Language: Python3
Software tool used: Jupyter Notebook (Anaconda Navigator)
Supporting file:

Create following files (Already included in submitted code)
1) "inputforbigrams.txt" containing corpous of the problem 2
2) "testbigramInput.txt" containing lines for the test input.

Programming imports:
import nltk
import random
import re
import numpy as np
from collections import Counter
from nltk.util import ngrams


Code description:

firstly the data is read through "inputforbigrams.txt" file for training courpos model. it is preprocess bu adding <s> and </s>syntaxes at the start and the end of the every sentence in the paragraph

