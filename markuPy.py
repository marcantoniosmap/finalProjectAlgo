import sublime
import sublime_plugin
import re 
import string

from .plytokenCopy import lerror
from .plyparseCopy import parser
from .parsing_HTML import run, levels


class MarkupyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = self.view.sel()[0] # first view cell
		region = self.view.line(region)
		between_tag = False
		error_syntax = False
		
		s = self.view.substr(region) # gets the string

		# checks the indentation based on the amount of tabs/whitespaces
		if s.startswith((' ')):
			tab_length = len(s) - len(s.strip())
			tab_length = int(tab_length / 4)
		elif s.startswith(('\t')):
			tab_length = len(s) - len(s.strip())
		elif s.startswith(''):
			tab_length = 0

		# if there is existing tags already
		if checkTag(s, tab_length) != -1:
			between_tag = True
			subbstring = checkTag(s, tab_length)
			s = s.replace(subbstring, '')
			mid = s.find('></')

			prev = parseSyn(subbstring, tab_length)
			if prev == -1:
				error_syntax = True
			else:
				mylist = prev.split("\n")

			if ("a" and "img") in subbstring and not error_syntax:
				temp = ""
				for i in range(len(mylist)):
					temp += mylist[i].strip()
				s = s[:mid+1] + temp + s[mid+1:]
			elif not error_syntax:
				temp = s[mid+1:]
				s = s[:mid+1]

				for i in range(len(mylist)):
					s = s + "\n" + "\t" + mylist[i]

				s = s + "\n" + "\t" * tab_length + temp
		else:
			s = parseSyn(s, tab_length)

		if not error_syntax and len(lerror) == 0:
			self.view.erase(edit, region)
			self.view.insert(edit, self.view.sel()[0].begin(), s)
		else:
			lregion = []
			index_between_tag = 0
			if between_tag:
				index_between_tag = (mid + 1)
			for item in lerror:
				s_error = region.begin() + item[0] + index_between_tag
				e_error = region.begin() + item[0] + item[1] + index_between_tag
				lregion.append(sublime.Region(s_error, e_error))
			self.view.add_regions('test', lregion, 'keyword', '', sublime.DRAW_NO_OUTLINE | sublime.DRAW_SOLID_UNDERLINE)
			lerror.clear()

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

def checkTag(s, tab_length):
	if '<' not in s:
		return -1
	elif '<' in s:
		posopn = s.find('</')
		tempo = s[:posopn].rfind('><') + 1
		if tempo >= 0:
			poscls = s[tempo:].find('>') + tempo + 1
		else:
			poscls = s.find('>')

		return s[poscls:posopn]

