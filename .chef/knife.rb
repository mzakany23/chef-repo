# See https://docs.chef.io/config_rb_knife.html for more information on knife configuration options

current_dir = File.dirname(__FILE__)
log_level                :info
log_location             STDOUT
node_name                "mzakany23"
client_key               "#{current_dir}/mzakany23.pem"
validation_client_name   "mzakany23-validator"
validation_key           "#{current_dir}/mzakany23-validator.pem"
chef_server_url          "https://api.opscode.com/organizations/mzakany23"
cache_type               'BasicFile'
cache_options( :path => "#{ENV['HOME']}/.chef/checksums" )
cookbook_path            ["#{current_dir}/../cookbooks"]
knife[:digital_ocean_access_token] = 'c479d23b1d2c185d2f027c983546976a7cebed387a661eddc2f6ec53178fdbba'