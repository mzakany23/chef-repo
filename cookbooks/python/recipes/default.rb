execute 'pip' do 
	command 'sudo apt-get -y install python-pip'
end

execute 'dependency' do 
	command 'sudo apt-get -y install python-dev'
end

execute 'dependency' do 
	command 'pip install setuptools==7.0'
end



