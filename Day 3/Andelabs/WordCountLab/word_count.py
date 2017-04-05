#!/usr/bin/env python
# encoding: utf-8

def words(message):
	words_counter = {}
	words_list = message.split()
	for word in words_list:
		if word in words_counter:
			words_counter[word] += 1
		else:
			words_counter[word] = 1
	print message
	print words_list
	print words_counter
	return words_counter
words('	this is 3 2		lemmah lemmah this	')
