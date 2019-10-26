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
		s = self.view.substr(region) # gets the string

		temp = parseSyn(s)

		if temp != -1:
			# self.view.erase(edit, region)
			print(self.view.rowcol(region.begin()))
			self.view.replace(edit, region, temp)


def parseSyn(s):
	global levels
	levels = 0
	result = parser.parse(s)
	# if syntax is right
	if not result is None:
		result = str(run(result))
		result = result[:-1]
		return result
	return -1
