package 'nginx' do 
	action :install
end

service 'nginx' do
  action [ :enable, :start ]
end

template "/etc/nginx/sites-available/default" do
  source "default.erb"
  mode '0755'
  owner 'root'
end

