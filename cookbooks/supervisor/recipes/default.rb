#
# Cookbook Name:: supervisor
# Recipe:: default
#
# Copyright 2015, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#

package 'install supervisor' do 
	action :install
end

execute 'make supervisor folder' do 
	folder = "/etc/supervisor/conf.d"
	command 'mkdir /etc/supervisor/conf.d'
	not_if {File.directory?(folder)}
end

template "/etc/supervisor/conf.d" do 
	source 'hello.conf'
	not_if {File.exists?("/etc/supervisor/conf.d")}
end

