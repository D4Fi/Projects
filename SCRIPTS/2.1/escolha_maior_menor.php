<?php
$number = rand(0, 10);
$start = true;

while ($start) {
     $user_number = readLine('Chute um numero:: ');
     if ($user_number > $number) {
         echo "Menor!\n";
     }
     else if ($user_number < $number) {
         echo "Maior!\n";
     }
     else if ($user_number == $number) {
         echo 'Você ganhou!';
         break;
     }
}
?>