h = DateTime.now.hour

package 'git' do 
	action :install
end

execute 'update' do 
	command 'sudo apt-get -y update'
	# only_if {h < 12}
end

execute 'upgrade' do 
	command 'sudo apt-get -y upgrade'
	# only_if {h < 12}
end


execute 'make app dir' do 
	cwd "/"
	command 'mkdir current'
	not_if {File.directory?('/current')}
end




