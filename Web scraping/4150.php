<?php # -*- coding: utf-8 -*-
/* Plugin Name: 4150 */	
add_shortcode('4150', 'HelloWorldShortcode4150');
function HelloWorldShortcode4150() {
ob_start();
chdir('/home/meteoda69/public_html/wp-content/plugins');
$var = file_get_contents( "4150.txt" );
echo $var;
$output = ob_get_clean();
    return $output;
}