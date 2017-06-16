#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import csv
import math
import random as rnd

def readProducts(filename):
	orders = pd.read_csv(filename)
	orderKeys = {}
	for index, row in orders.iterrows():
		qty = 0
		if "None" not in row["products"]:
			qty = len(str(row["products"]).split(" "))
		orderKeys[row["order_id"]]=qty
		print(str(index)+"/"+str(len(orders.index)))
	return orderKeys

def readCustomerOrders(filename):
	orders = pd.read_csv(filename)
	return orders

print("READ PRODUCTS")
products = readProducts("../data/summarized/train_orders_products.csv")
print("READ ORDERS")
orders = readCustomerOrders("../data/summarized/train_orders.csv")

data={}
for index, row in orders.iterrows():
	if row["order_id"] in products.keys():
		if row["user_id"] not in data.keys():
			data[row["user_id"]] = []
		data[row["user_id"]].append(products[row["order_id"]])
		print(str(index)+"/"+str(len(orders.index)))


empty_trend = open("../data/empty/train.csv", 'w',  newline='')
spamwriter = csv.writer(empty_trend, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamwriter.writerow(["user_id", "qty_products"])
counter = 0
for user in data.keys():
	spamwriter.writerow([user, ",".join([str(x) for x in data[user]])])
	counter+=1
	print("WRITING: "+str(counter)+"/"+str(len(data.keys())))