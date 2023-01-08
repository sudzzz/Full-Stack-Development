<?php

$tb = "";
$tr = "";
$ctr = 1;

foreach(file('mydata.txt') as $line){
    $tr = $tr."<tr><td>".$ctr."</td><td>".$line."</td></tr>";
    $ctr += 1;
}
$tb = "<table border=1>".$tr."</table>";
echo $tb;

?>