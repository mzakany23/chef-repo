# See https://docs.chef.io/config_rb_knife.html for more information on knife configuration options

current_dir = File.dirname(__FILE__)
log_level                :info
log_location             STDOUT
node_name                "mzakany23"
client_key               "#{current_dir}/mzakany23.pem"
validation_client_name   "mzakany23-validator"
validation_key           "#{current_dir}/mzakany23-validator.pem"
chef_server_url          "https://api.opscode.com/organizations/mzakany23"
cookbook_path            ["#{current_dir}/../cookbooks"]
