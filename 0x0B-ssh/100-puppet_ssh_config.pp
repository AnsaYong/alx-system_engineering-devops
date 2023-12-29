# A manifest that sets up the client SSH configuration file so that
# you can connect to a server without typing a password
#
# This class uses the `ssh_authorized_key` approach rather than the
# `file_line` approach
class ssh_config {
  # Define class for managing SSH configuration

  # Set up SSH key authentication
  ssh_authorized_key { 'school':
    ensure => present,
    user   => 'ubuntu',             # Username
    type   => 'ssh-rsa',            # type of key
    key    => '~/.ssh/school.pub',  # path to the public key
  }

  # Disable password authentication
  file { '/etc/ssh/sshd_config':
    ensure  => present,
    owner   => 'root',
    group   => 'root',
    mode    => '0744',
    content => template('ssh_config/ssh_config.erb'),
    notify  => Service['ssh'],
  }

  service { 'ssh':
    ensure  => running,
    enable  => true,
    require => File['/etc/ssh/sshd_config'],
  }
}
