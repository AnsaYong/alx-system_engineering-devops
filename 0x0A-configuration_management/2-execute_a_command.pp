# A manifest that kills a process named killmenow


exec { 'kill_killmenow_process':
  path    => '/usr/bin/',
  command => 'pkill -f killmenow',
}
