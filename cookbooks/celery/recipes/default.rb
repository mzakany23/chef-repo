execute 'install celery' do 
	command 'pip install celery'
end

execute 'install django-celery' do 
	command 'pip install django-celery'
end

execute 'install redis-server' do 
	command 'sudo apt-get -y install redis-server'
end

	
