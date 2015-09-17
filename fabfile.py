from env_var import ENV
from fabric.api import lcd,prefix,env,local,run

class StaticFileManagment:
	def __init__(self,**kwargs):
		self.server_ip      = kwargs['server_ip']
		self.local_home_dir = kwargs['local_home_dir']
		self.app_name       = kwargs['app_name']
		self.local_root_dir = kwargs['local_root_dir']
		self.host_root_dir  = kwargs['host_root_dir']

	def push_static_files_to_host(self):
		self._collect_static()
		self._rsync_cp_to_host()

	# private
	def _collect_static(self):
		with lcd(self.local_home_dir):
			with prefix('source %sbin/activate' % self.local_home_dir):
				with lcd(self.app_name):
					local("python manage.py collectstatic")

	def _rsync_cp_to_host(self):
		# rsync -avz root/ root@45.55.231.143:/root/
		local("rsync -avz %s root@%s:%s" % (self.local_root_dir,self.server_ip,self.host_root_dir))


def push_static():
	static_server = StaticFileManagment(
			server_ip=ENV['host_ip'],
			local_home_dir='/Users/mzakany/Desktop/jmi_fundraising/',
			app_name='jmi',
			local_root_dir='/Users/mzakany/Desktop/jmi_fundraising/static/root/',
			host_root_dir='/current/root/',
			)
	static_server.push_static_files_to_host()



