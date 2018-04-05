# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:00:36 2017

@author: kiran
"""

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
# things we need for Tensorflow
import numpy as np
import tflearn
import tensorflow as tf
import random
import json
(model.predict([p]))
import pickle

