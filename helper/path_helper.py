import os

class PathHelper(object):
	def __init__(self,**kwargs):
		self.local_home_dir = kwargs['local_home_dir']
		self.local_app_name = kwargs['local_app_name']
		
		try:
			self.host_ip         = kwargs['host_ip']
			self.host_static_dir = kwargs['host_static_dir']
			self.host_main_dir   = kwargs['host_main_dir']
		except:
			self.host_ip         = None
			self.host_static_dir = None
			self.host_main_dir   = None
		

	def get_static_dir_absolute_path(self):
		static_path = self.local_home_dir+'/static/'
		return os.path.abspath(static_path) if os.path.exists(static_path) else False

	def get_app_path(self):
		app_path = self.local_home_dir+'/'+self.local_app_name
		return os.path.abspath(self.local_home_dir+'/'+self.local_app_name) if os.path.exists(app_path) else False



