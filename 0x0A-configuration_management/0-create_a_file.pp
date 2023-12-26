# Creates a file `school` in tmp and assigns permissions
# owner, group, and has a specific text

file { '/tmp/school':
  ensure  => 'file',          # Ensure that it's a file
  mode    => '0744',          # Set the file permissions (no special, owner: read/write/execute, group: read, others: read)
  owner   => 'www-data',      # Set the file owner
  group   => 'www-data',      # Set the file group
  content => 'I love Puppet', # Set the file content
}
