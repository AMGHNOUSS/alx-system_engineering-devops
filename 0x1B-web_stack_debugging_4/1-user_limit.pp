# Enable the user holbertoon to login and open files.

exec { 'hard-file':
  command => 'sed -i "/holbertoon hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'soft-file':
  command => 'sed -i "/holbertoon soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
