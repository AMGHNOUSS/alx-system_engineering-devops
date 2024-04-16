# Fix problem of Apache returning 500 errors.

exec { 'replace':
	provider => shell,
	command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
