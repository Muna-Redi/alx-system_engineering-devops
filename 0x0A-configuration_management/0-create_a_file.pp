# This maniefest creates a file with given permissions and ownerships
file {'/tmp/school/':
  ensure  => file,
  path    => '/tmp/school',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}
