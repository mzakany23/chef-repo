#
# Cookbook Name:: supervisor
# Recipe:: default
#
# Copyright 2015, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#

package 'supervisor' do 
	action :install
end

template "/etc/supervisor/supervisord.conf" do 
	source 'supervisord.erb'
end

