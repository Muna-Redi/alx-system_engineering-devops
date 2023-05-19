# puppet script to allow user holberton to login and open files without errors

# permitting  hard file access for user holberton
exec { 'permit-hard-file-handling':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# permitting soft file access for user holberton
exec { 'permit-soft=file-handling':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
