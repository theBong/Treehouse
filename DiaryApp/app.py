#!/usr/bin/env python3
import datetime as datetime
from collections import OrderedDict
import os
import sys

from peewee import *

db = SqliteDatabase('diary.db')



class Entry(Model):
	#content
	#timestamp

	content = TextField()
	timestamp = DateField(default = datetime.datetime.now) #not now() otherwise datetime is stored for time it is run, not when entry is created.

	class Meta:
		database = db

def clear():
	os.system('clear')

def initialize():
	""" Create database and table if they don't exist"""
	db.connect()
	db.create_tables([Entry], safe=True)

def menu_loop():
	choice = None
	clear()
	while choice != 'q':
		print("Enter q to quit:")
		for key, value in menu.items():
			print (key, value.__doc__)
		choice = input('Actions: ').lower().strip()
		if choice in menu:
			menu[choice]()

def add_entry():
	"""Add an Entry"""
	print("Enter entry so it can be entered into the entry. Press Ctrl+D when finished")
	data = sys.stdin.read().strip()

	if data:
		Entry.create(content=data)
		print("\nSaved yo!")

def view_entries(search=None):
	"""View Entries"""
	entries = Entry.select().order_by(Entry.timestamp.desc())
	if search:
		entries = entries.where(Entry.content.contains(search))
	for entry in entries:
		timestamp = entry.timestamp.strftime('%A %B %d, %y %I:%M%p')
		print(timestamp)
		print('='*len(timestamp))
		print(entry.content)
		print('\nn)next entry\nd)Delete entries\nq)return to main menu\n')
		next_action = input('Action: [Nq]').lower().strip()

		if next_action == 'q':
			break
		elif next_action == 'd':
			delete_entry(entry)

def search_entries():
	'''Search through the entries'''
	view_entries(input("Enter search query: "))


def delete_entry(entry):
	"""Delete  entry"""
	entry.delete_instance()

	
menu = OrderedDict([
		('a', add_entry),
		('v', view_entries),
		('s', search_entries)
	])

if __name__ == '__main__':
	initialize()

	menu_loop()