<?php
class MetodoIniciador {
    private $nome;
    private $idade;
    function __construct($nome, $idade) {
        $this->nome = $nome;
        $this->idade = $idade;
    }

    public function str() {
        print "nome: $this->nome, idade: $this->idade";
    }
}

$teste = new MetodoIniciador('lucas', '23');

$teste->str();
?>