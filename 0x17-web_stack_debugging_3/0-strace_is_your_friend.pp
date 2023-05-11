# puppet script to fix an error in a line in a file on a server

$file_name = '/var/www/html/wp-settings.php'

exec { 'fix_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
