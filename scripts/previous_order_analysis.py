#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import csv
import math
import random as rnd


def count_similarity(list1, list2):
	return len(set(list1) & set(list2))


product_orders = pd.read_csv("../data/summarized/grouped_prior_orders", delimiter=',',
                        quotechar='|')
orders = pd.read_csv("../data/summarized/prior_order_user.csv").set_index('order_id')['user_id'].to_dict()


data ={}
for index, row in product_orders.iterrows():
	if row["order_id"] in orders.keys():
		if orders[row["order_id"]] not in data.keys():
			data[orders[row["order_id"]]] = { "previous_order":[], "previous_order_products":[], "reordered_previous_order":[], "second_order":[], "second_order_products":[], "reordered_second_order":[], "third_order":[], "third_order_products":[], "reordered_third_order":[], "fourth_order":[], "fourth_order_products":[], "reordered_fourth_order":[], "fifth_order":[], "reordered_fifth_order":[], "fifth_order_products":[] }
		if len(data[orders[row["order_id"]]]["fifth_order_products"])>0:
			products = row["products"].split(",")
			similarity = count_similarity(data[orders[row["order_id"]]]["fifth_order_products"], products)
			data[orders[row["order_id"]]]["fifth_order"].append(similarity)
			reordered = 0
			if row["reordered"] > 0:
				reordered = round(float(similarity)/float(reordered),2)
			data[orders[row["order_id"]]]["reordered_fifth_order"].append(reordered)
		if len(data[orders[row["order_id"]]]["fourth_order_products"])>0:
			products = row["products"].split(",")
			similarity = count_similarity(data[orders[row["order_id"]]]["fourth_order_products"], products)
			data[orders[row["order_id"]]]["fourth_order"].append(similarity)
			reordered = 0
			if row["reordered"] > 0:
				reordered = round(float(similarity)/float(reordered),2)
			data[orders[row["order_id"]]]["reordered_fourth_order"].append(reordered)
			data[orders[row["order_id"]]]["fifth_order_products"] = data[orders[row["order_id"]]]["fourth_order_products"]
		if len(data[orders[row["order_id"]]]["third_order_products"])>0:
			products = row["products"].split(",")
			similarity = count_similarity(data[orders[row["order_id"]]]["third_order_products"], products)
			data[orders[row["order_id"]]]["third_order"].append(similarity)
			reordered = 0
			if row["reordered"] > 0:
				reordered = round(float(similarity)/float(reordered),2)
			data[orders[row["order_id"]]]["reordered_third_order"].append(reordered)
			data[orders[row["order_id"]]]["fourth_order_products"] = data[orders[row["order_id"]]]["third_order_products"]
		if len(data[orders[row["order_id"]]]["second_order_products"])>0:
			products = row["products"].split(",")
			similarity = count_similarity(data[orders[row["order_id"]]]["second_order_products"], products)
			data[orders[row["order_id"]]]["second_order"].append(similarity)
			reordered = 0
			if row["reordered"] > 0:
				reordered = round(float(similarity)/float(reordered),2)
			data[orders[row["order_id"]]]["reordered_second_order"].append(reordered)
			data[orders[row["order_id"]]]["third_order_products"] = data[orders[row["order_id"]]]["second_order_products"]
		if len(data[orders[row["order_id"]]]["previous_order_products"])>0:
			products = row["products"].split(",")
			similarity = count_similarity(data[orders[row["order_id"]]]["previous_order_products"], products)
			data[orders[row["order_id"]]]["previous_order"].append(similarity)
			reordered = -1
			if row["reordered"] > 0:
				reordered = round(float(similarity)/float(reordered),2)
			data[orders[row["order_id"]]]["reordered_previous_order"].append(reordered)
			data[orders[row["order_id"]]]["second_order_products"] = data[orders[row["order_id"]]]["previous_order_products"]
		data[orders[row["order_id"]]]["previous_order_products"] = row["products"].split(",")
	print(str(index)+"/"+str(len(product_orders.index)))





previous_order = open("../data/previous_order/previous_order.csv", 'w',  newline='')
spamwriter = csv.writer(previous_order, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamwriter.writerow(["user_id", "avg", "avg_percent", "from_previous", "percent_previous"])

second_order = open("../data/previous_order/second_order.csv", 'w',  newline='')
spamwriter_second = csv.writer(second_order, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamwriter_second.writerow(["user_id", "avg", "avg_percent","from_previous", "percent_previous"])

third_order = open("../data/previous_order/third_order.csv", 'w',  newline='')
spamwriter_third = csv.writer(third_order, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamwriter_third.writerow(["user_id", "avg","avg_percent", "from_previous", "percent_previous"])

fourth_order = open("../data/previous_order/fourth_order.csv", 'w',  newline='')
spamwriter_fourth = csv.writer(fourth_order, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamwriter_fourth.writerow(["user_id", "avg","avg_percent", "from_previous", "percent_previous"])

fifth_order = open("../data/previous_order/fifth_order.csv", 'w',  newline='')
spamwriter_fifth = csv.writer(fifth_order, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamwriter_fifth.writerow(["user_id", "avg","avg_percent", "from_previous", "percent_previous"])

counter=0
for user in data.keys():
	avg_percent = -1
	avg=-1
	if len(data[user]["previous_order"])>0:
		avg = round(float(sum(data[user]["previous_order"]))/float(len(data[user]["previous_order"])),2)
	if len(data[user]["reordered_previous_order"])>0:
		avg_percent = round(float(sum([x for x in data[user]["reordered_previous_order"] if x != -1]))/float(len(data[user]["reordered_previous_order"])),2)
	spamwriter.writerow([user, avg, avg_percent, ",".join([str(x) for x in data["user"]["previous_order"]]), ",".join([str(x) for x in data["user"]["reordered_previous_order"]])])

	avg_percent = -1
	avg=-1
	if len(data[user]["second_order"])>0:
		avg = round(float(sum(data[user]["second_order"]))/float(len(data[user]["second_order"])),2)
	if len(data[user]["reordered_second_order"])>0:
		avg_percent = round(float(sum([x for x in data[user]["reordered_second_order"] if x != -1]))/float(len(data[user]["reordered_second_order"])),2)
	spamwriter_second.writerow([user, avg, avg_percent, ",".join([str(x) for x in data["user"]["second_order"]]), ",".join([str(x) for x in data["user"]["reordered_second_order"]])])

	avg_percent = -1
	avg=-1
	if len(data[user]["third_order"])>0:
		avg = round(float(sum(data[user]["third_order"]))/float(len(data[user]["third_order"])),2)
	if len(data[user]["reordered_third_order"])>0:
		avg_percent = round(float(sum([x for x in data[user]["reordered_third_order"] if x != -1]))/float(len(data[user]["reordered_third_order"])),2)
	spamwriter_third.writerow([user, avg, avg_percent, ",".join([str(x) for x in data["user"]["third_order"]]), ",".join([str(x) for x in data["user"]["reordered_third_order"]])])

	avg_percent = -1
	avg=-1
	if len(data[user]["fourth_order"])>0:
		avg = round(float(sum(data[user]["fourth_order"]))/float(len(data[user]["fourth_order"])),2)
	if len(data[user]["reordered_fourth_order"])>0:
		avg_percent = round(float(sum([x for x in data[user]["reordered_fourth_order"] if x != -1]))/float(len(data[user]["reordered_fourth_order"])),2)
	spamwriter_fourth.writerow([user, avg, avg_percent, ",".join([str(x) for x in data["user"]["fourth_order"]]), ",".join([str(x) for x in data["user"]["reordered_fourth_order"]])])

	avg_percent = -1
	avg=-1
	if len(data[user]["fifth_order"])>0:
		avg = round(float(sum(data[user]["fifth_order"]))/float(len(data[user]["fifth_order"])),2)
	if len(data[user]["reordered_fifth_order"])>0:
		avg_percent = round(float(sum([x for x in data[user]["reordered_fifth_order"] if x != -1]))/float(len(data[user]["reordered_fifth_order"])),2)
	spamwriter_fifth.writerow([user, avg, avg_percent, ",".join([str(x) for x in data["user"]["fifth_order"]]), ",".join([str(x) for x in data["user"]["reordered_fifth_order"]])])

	counter+=1
	print(str(counter)+"/"+str(len(data.keys())))
