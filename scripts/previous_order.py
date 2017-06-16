#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import csv
import math

#order_id,product_id,add_to_cart_order,reordered

csv_orders = pd.read_csv("../data/official/order_products__prior.csv")

orders = {}

for index, row in csv_orders.iterrows():
	if int(row["order_id"]) not in orders.keys():
		orders[int(row["order_id"])]={"reordered":0, "products":[]}
	orders[int(row["order_id"])]["products"].append(int(row["product_id"]))
	if int(row["reordered"])==1:
		orders[int(row["order_id"])]["reordered"]+=1
	print(str(index)+"/"+str(len(csv_orders.index)))

empty_trend = open("../data/summarized/grouped_prior_orders.csv", 'w',  newline='')
spamwriter = csv.writer(empty_trend, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamwriter.writerow(["order_id", "reordered", "products"])
for order in orders.keys():
	spamwriter.writerow([order, orders[order]["reordered"], ",".join([ str(x) for x in orders[order]["products"]]) ])
