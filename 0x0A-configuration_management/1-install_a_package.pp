# Installs Flask using pip3
package { 'python3-pip':
  ensure => installed,
}

# Upgrade pip to verson 20.0.2
exec { 'upgrade_pip':
  command => '/usr/bin/pip3 install --upgrade pip==20.0.2',
  unless  => '/usr/bin/pip3 show pip | grep Version | grep -q 20.0.2',
  require => Package['python3-pip'],
}

# Install version 2.1.0 of Flask using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask -v 2.1.0',   # Specify the desired version
  unless  => '/usr/bin/pip3 show Flask | grep Version | grep -q 2.1.0', # Check if Flask is already installed with the desired version
  require => Exec['upgrade_pip'],                    # Ensure that pip3 is installed before running the exec
}
