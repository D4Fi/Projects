<?php
$x =  readline('Enter a string: ');
$piramide = '';
for ($i = 1; $i <= $x; $i++) {
   for ($ii = 1; $ii <= $i; $ii++) {
       echo strval($i);
   }
   echo "\n";
}
?>