#
# Cookbook Name:: gunicorn
# Recipe:: default
#
# Copyright 2015, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#
INSTALLED = '/webapps/django-app/lib/python2.7/site-packages'

execute 'install gunicorn' do 
	cwd "/webapps/django-app"
	command "bin/pip install gunicorn"
	not_if {Dir.entries(INSTALLED).to_s.include?("gunicorn")}
end

execute 'install psycopg2' do 
	cwd "/webapps/django-app"
	command "bin/pip install psycopg2"
	not_if {Dir.entries(INSTALLED).to_s.include?("psycopg2")}
end

package 'python-dev' do 
	action :install
end

package 'supervisor' do 
	action :install
end
