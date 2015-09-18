from fabric.api import lcd,prefix,env,local,run
from path_helper import PathHelper

class StaticFileManagment(PathHelper):
	def __init__(self,**kwargs):
		super(StaticFileManagment,self).__init__(**kwargs)

	def push_static_files_to_host(self):
		self._collect_static()
		self._rsync_cp_to_host()

	# private
	def _collect_static(self):
		with lcd(self.local_home_dir):
			with prefix('source %sbin/activate' % self.local_home_dir):
				with lcd(self.get_app_path()):
					local("python manage.py collectstatic")

	def _rsync_cp_to_host(self):
		# rsync -avz root/ root@45.55.231.143:/root/
		# rsync -avz --exclude '.git*' --exclude 'static/static' --exclude 'static/media' --exclude 'static/root' source_dir/ new_dir/
		local("rsync -avz %s/root root@%s:%s" % (self.get_static_dir_absolute_path,self.host_ip,self.host_static_dir))
		local("rsync -avz %s/media root@%s:%s" % (self.get_static_dir_absolute_path,self.host_ip,self.host_static_dir))


		
		
