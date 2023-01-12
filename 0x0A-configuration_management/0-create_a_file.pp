#This maniefest creates a file with given permissions and ownerships

file {"/tmp/school/":
  ensure => file,
  path => "/tmp/school",
  content => "I Love Puppet",
  owner => "www-data",
  group => "www-data",
  mode => 744
}
