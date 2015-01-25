#
# Cookbook Name:: base
# Recipe:: default
#
# Copyright 2015, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#

APP_PATH = '/webapps/django-app/'
VIRTUAL_ENV_PATH = 'bin/python'
INSTALLED = '/webapps/django-app/lib/python2.7/site-packages'

h = DateTime.now.hour

package 'psycopg2' do 
	action :install
end

execute 'update' do 
	command 'sudo apt-get -y update'
	only_if {h < 12}
end

package 'git' do 
	action :install
end

execute 'upgrade' do 
	command 'sudo apt-get -y upgrade'
	only_if {h < 12}
end

package 'python-virtualenv' do 
	action :install
end

execute 'make dir' do 
	command "sudo mkdir -p #{APP_PATH}"
	not_if {File.directory?(APP_PATH)}
end

execute 'make env' do 
	cwd "/webapps/django-app"
	command 'virtualenv .'
	not_if {File.directory?('/webapps/django-app/bin')}
end

execute 'install django' do 
	cwd "/webapps/django-app"
	command "bin/pip install django"
	not_if {Dir.entries(INSTALLED).to_s.include?("django")}
end


