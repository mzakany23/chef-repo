['postgresql','postgresql-contrib'].each do |p|
	package p do 
		action :install
	end
end