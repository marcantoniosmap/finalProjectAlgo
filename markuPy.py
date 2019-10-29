import sublime
import sublime_plugin
import re 
import string

from .plyparseCopy import parser
from .parsing_HTML import run, levels


class MarkupyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = self.view.sel()[0] # first view cell
		region = self.view.line(region)
		
		tab_length = len(self.view.substr(region))
		tab_length -= len(self.view.substr(region).strip())

		s = self.view.substr(region) # gets the string

		if checkTag(s) != -1:
			print("asdf")
			subbstring = checkTag(s)
			s = s.replace(subbstring, '')
			mid = s.find('></')

			mylist = parseSyn(subbstring, tab_length).split("\n")

			if ("a" or "img") in subbstring:
				temp = ""
				for i in range(len(mylist)):
					temp += mylist[i].strip()
				print(temp)
				s = s[:mid+1] + temp + s[mid+1:]
				print(s)
			else:
				# if between tag and the tag != headers/p
				temp = s[mid+1:]
				s = s[:mid+1]
				second_tab = int((mid - tab_length) / 3)
				print(second_tab)

				for i in range(len(mylist)):
					s = s + "\n" + "\t" * (second_tab) + mylist[i]

				s = s + "\n" + "\t" * tab_length + temp
			self.view.erase(edit, region)
			self.view.insert(edit, self.view.sel()[0].begin(), s)

		temp = parseSyn(s, tab_length)

		if temp != -1:
			self.view.erase(edit, region)
		# 	# self.view.replace(edit, region, "\t" * length)
		# 	# temp = ""
		# 	# for i in range(len(mylist)):
		# 	# 	temp += "\t" * tab_length
		# 	# 	temp += mylist[i]
		# 	# 	temp += "\n"
		# 	# temp = temp[:-1]
			self.view.insert(edit, self.view.sel()[0].begin(), temp)


def parseSyn(s, tab_length):
	global levels
	levels = 0
	result = parser.parse(s)
	# if syntax is right
	if not result is None:
		result = str(run(result))
		result = result[:-1]
		list = result.split("\n")

		temp = ""
		for i in range(len(list)):
			temp += "\t" * tab_length
			temp += list[i]
			temp += "\n"
		temp = temp[:-1]

		return temp
	return -1

def checkTag(s):
	if '<' not in s:
		return -1
	elif '<' in s:
		index = 0
		n = int(len(s) / 2)
		while index < len(s):
			index = s[:n].find('<', index)
			if index == -1:
				break
			pos = index
			index += 1
		s = s[pos + 1:]

		poscls = s.find('>') + 1
		posopn = s.find('<')
		# print("{} {}".format(poscls, posopn))
		return s[poscls:posopn]

