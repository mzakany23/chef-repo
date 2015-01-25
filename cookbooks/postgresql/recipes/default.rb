#
# Cookbook Name:: postgresql
# Recipe:: default
#
# Copyright 2015, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#


['postgresql','postgresql-contrib','libpq-dev', 'python-dev'].each do |p|
	package p do 
		action :install
	end
end