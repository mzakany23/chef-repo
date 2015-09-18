from jsmin import jsmin
from cssmin import cssmin

import os
from fnmatch import fnmatch
from os import listdir
from os.path import isfile, join, isdir, abspath
from fabric.api import lcd,prefix,env,local,run


class Minify:
	def __init__(self,root_dir):
		self.root_dir = root_dir
		self.base_project_folder = '/jmi_fundraising/' in self.root_dir
	
	def minify_css(self):
		for root, dirs, files in os.walk(self.root_dir, topdown=False):
			for name in files:
				file = join(root,name)
				if fnmatch(file,'*.css') and not fnmatch(file,'*min.css'):
					if not self.base_project_folder:
						self._minify_css(file)

	def minify_js(self):
		for root, dirs, files in os.walk(self.root_dir, topdown=False):
			for name in files:
				file = join(root,name)
				if fnmatch(file,'*.js') and not fnmatch(file,'*min.js'):
					if not self.base_project_folder:
						self._minify_js(file)
					

	# private

	def _minify_js(self,file):
		with open(file) as js_file:
			minified = jsmin(js_file.read())
		with open(file,'w+') as js:
			js.write(minified)
	
	def _minify_css(self,file):
		with open(file) as css_file:
			minified = cssmin(css_file.read())
		with open(file,'w+') as css:
			css.write(minified)
					

# m = Minify('/Users/mzakany/Desktop/jmi_fundraising 8/static/root')

# # print m.minify_js()
# print m.minify_css()