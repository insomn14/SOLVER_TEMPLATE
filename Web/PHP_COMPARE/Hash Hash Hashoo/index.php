<?php
    if( isset($_GET['a']) && isset($_GET['b']) ) {
        if ( $_GET['a'] !== $_GET['b'] ) {
            if ( md5($_GET['a']) === md5($_GET['b']) ) {

                $flagFile = fopen("/var/flag", "r");
                $flag = fread($flagFile, filesize("/var/flag"));
                fclose($flagFile);

                echo $flag;
                
            } else {
                echo "hash nya harus sama!";
            }
        } else {
            echo "value nya gaboleh sama!";
        }
    } else {
        highlight_file(__file__);
    }
?>
