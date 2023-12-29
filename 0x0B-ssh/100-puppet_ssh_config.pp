# A manifest that sets up the client SSH configuration file so that
# you can connect to a server without typing a password
#
# This class uses the `file_line` approach rather than the
# `ssh_authorized_key` approach
class ssh_config {
  # Define class for managing SSH configuration
  # Set up SSH key authentication using the file_line approach

  # Turn off password authentication
  file_line { 'Turn off password authentication':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',  # replaces the line in the file that matches the pattern below
    match  => '^#?\s*PasswordAuthentication\s+.*$', # pattern to find in the file
  }

  # specify the identify file - contains the RSA private key
  file_line { 'Declare identity file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
    match  => '^#?\s*IdentityFile\s+.*$',
  }

  # Reload the SSH service when the configuration changes
  service { 'ssh':
    ensure  => running,
    enable  => true,
    require => [File_line['Turn off password authentication'], File_line['Declare identity file']],
  }
}
