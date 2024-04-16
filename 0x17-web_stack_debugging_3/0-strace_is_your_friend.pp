# Fix problem of Apache returning 500 errors.

exec { 'fix-error':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path => '/usr/local/bin/:/bin'
}
