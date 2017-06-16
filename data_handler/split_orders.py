#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import csv
import math
import random as rnd



orders = pd.read_csv("../data/official/orders.csv")

orders.set_index("eval_set", inplace=True)

prior = orders.loc["prior"]
prior.to_csv("../data/summarized/prior_orders.csv")

train = orders.loc["train"]
train.to_csv("../data/summarized/train_orders.csv")

test = orders.loc["test"]
test.to_csv("../data/summarized/test_orders.csv")