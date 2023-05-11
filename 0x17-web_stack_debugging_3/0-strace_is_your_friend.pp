# puppet script to fix an error in a line in a file on a server

$file_name = '/var/www/html/wp-settings.php'
$file_path = ['/bin','/usr/bin']

exec { 'fix_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => "${file_path}"
}
