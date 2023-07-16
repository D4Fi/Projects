<?php
$itens_compra = ["Arroz", "Leite", "Ovos", "Feijão", "Tomate"];
$count = 0;

foreach ($itens_compra as $value) {
  echo "item: $count $value\n";
  $count += 1;
}
?>