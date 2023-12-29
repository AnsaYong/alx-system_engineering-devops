# A manifest that sets up SSH key authentication by using the
# file_line approach to update the client SSH configuration file
# to allow connection to a server without typing a password

# Set up SSH key authentication using the file_line approach

# Turn off password authentication
file_line { 'Turn off password authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',  # replaces the line in the file that matches the pattern below
  match  => '#    PasswordAuthentication yes', # line in the file to replace
}

# specify the identify file - contains the RSA private key
file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school', # add line that contains the RSA private key
}
