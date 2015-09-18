import sys 

sys.path.append('helper')

from fabric.api import lcd,prefix,env,local,run
from env_var import ENV
from minify import Minify
from os.path import join, isdir, abspath, dirname, realpath

production_app_name  = 'jmi_fundraising_production'
production 			 = join(dirname(realpath(__file__)),'production')
production_base_path = join(production, production_app_name)
tmp_exists 			 = isdir(production)
app_name			 = 'jmi'

app_host			 = '45.55.47.208'
cdn_host			 = '45.55.175.19'

def make_local_production_copy():
	with lcd('/Users/mzakany/Desktop'):		
		local("rsync -avz --exclude '.git*' --exclude '.gitignore' /Users/mzakany/Desktop/jmi_fundraising/ %s/jmi_fundraising_production/" % production)

def collectstatic():
	with lcd(production_base_path):
		with prefix('source %s/bin/activate' % production_base_path):
			with lcd(app_name):
				local('python manage.py collectstatic')

def minify_assets():
	m = Minify('%s/static/root' %production_base_path)
	m.minify_js()
	m.minify_css()

def deploy_app_to_host():
	local("rsync -avz --exclude 'static/static' --exclude 'static/media' --exclude 'static/root' %s/ root@%s:/current/%s/" % (production_base_path, app_host, production_app_name ))
	
def deploy_static_files():
	local('rsync -avz %s/static/root root@%s:/current/root/' % (production_base_path, cdn_host))
	local('rsync -avz %s/static/media root@%s:/current/media/' % (production_base_path, cdn_host))




	