# -*- coding: utf-8 -*-
#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction import DictVectorizer
import sys
from collections import defaultdict
from sklearn.decomposition import PCA


datasets_file = "sma++_data.txt"
morph_dataset_dict = []
morph_dataset_strings = open(datasets_file)

for datapoint in morph_dataset_strings:
    datapoint = datapoint.split(',')
    datapoint_dict = defaultdict()

    datapoint_dict['current_token'] = datapoint[0]
    datapoint_dict['POS'] = datapoint[1]
    datapoint_dict['suffix_1'] = datapoint[2]
    datapoint_dict['suffix_2'] = datapoint[3]
    datapoint_dict['suffix_3'] = datapoint[4]
    datapoint_dict['suffix_4'] = datapoint[5]
    datapoint_dict['suffix_5'] = datapoint[6]
    datapoint_dict['suffix_6'] = datapoint[7]
    datapoint_dict['suffix_7'] = datapoint[8]
    datapoint_dict['G_prev1'] = datapoint[9]
    datapoint_dict['G_prev2'] = datapoint[10]
    datapoint_dict['G_prev3'] = datapoint[11]
    datapoint_dict['N_prev1'] = datapoint[12]
    datapoint_dict['N_prev2'] = datapoint[13]
    datapoint_dict['N_prev3'] = datapoint[14]
    datapoint_dict['P_prev1'] = datapoint[15]
    datapoint_dict['P_prev2'] = datapoint[16]
    datapoint_dict['P_prev3'] = datapoint[17]
    datapoint_dict['C_prev1'] = datapoint[18]
    datapoint_dict['C_prev2'] = datapoint[19]
    datapoint_dict['C_prev3'] = datapoint[20]
    datapoint_dict['G_next1'] = datapoint[21]
    datapoint_dict['N_next1'] = datapoint[22]
    datapoint_dict['P_next1'] = datapoint[23]
    datapoint_dict['C_next1'] = datapoint[24]
    datapoint_dict['token_prev'] = datapoint[25]
    datapoint_dict['token_next'] = datapoint[26]
    datapoint_dict['len_curr_tok'] = datapoint[-2]
    datapoint_dict['chartype_curr_tok'] = datapoint[-1]

    morph_dataset_dict.append(datapoint_dict)

vec = DictVectorizer()
morph_dataset2 = vec.fit(morph_dataset_dict)

vocab = morph_dataset2.vocabulary_
print vocab
