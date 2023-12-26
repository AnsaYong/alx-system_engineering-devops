# Installs Flask using pip3


# Ensure that pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install version 2.1.0 of Flask using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',   # Specify the desired version
  path    => ['/usr/bin'],                           # Set the pah to include pip3
  unless  => '/usr/bin/pip3 show Flask | grep Version | grep -q 2.1.0', # Check if Flask is already installed with the desired version
  require => Package['python3-pip'],                 # Ensure that pip3 is installed before running the exec
}
