# Fix bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

file { '/var/www/html/wp-settings.php':
ensure  => file,
content => file('/var/www/html/wp-settings.php').content.gsub('phpp', 'php'),
}
