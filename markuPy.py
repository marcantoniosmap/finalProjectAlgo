# import sublime
# import sublime_plugin
# import re 
# import string

from .plyparseCopy import parser

class MarkuPyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = self.view.sel()[0] # first view cell
		region = self.view.line(region)
		s = self.view.substr(region) # gets the string

		temp = parseSyn(s)

		self.view.erase(edit, region)
		self.view.insert(edit, 0, temp)


def parseSyn(s):
	result = parser.parse(s)
	temp = str(result)
	return temp
