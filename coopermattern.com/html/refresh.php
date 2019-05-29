<?php
    $output = shell_exec('/usr/bin/python3 /var/www/flightdata.py');
    shell_exec('/usr/bin/python3 /var/www/webpage.py');
    echo "<h1> $output </h1>";
?>
