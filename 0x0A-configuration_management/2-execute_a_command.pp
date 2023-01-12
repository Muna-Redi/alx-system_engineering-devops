# manifest to kill a program named 'killmenow'
exec{ 'killmenow':
  command => 'pkill -15 killmenow',
  path    => '/usr/bin/'
}
