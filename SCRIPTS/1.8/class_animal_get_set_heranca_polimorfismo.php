<?php
class Animal {
    private $idade;
    private $cor;

    function __construct($idade, $cor) {
        $this->idade = $idade;
        $this->cor = $cor;
    }

    public function getIdede() {
        return $this->idade;
    }

    public function getCor() {
        return $this->cor;
    }

    public function setIdade($newIdade) {
        $this->idade = $newIdade;
    }

    public function setCor($neWcor) {
        $this->cor = $newCor;
    }

    public function falar() {
        echo 'Não fala!';
    }

    public function __str__() {
        print "Idade: $this->idade\nCor: $this->cor\n";

    }
}

class Cachorro extends Animal {
    public function falar() {
        echo 'Falar: Auu Auuu!';
    }
}

class Gato extends Animal {
    public function falar() {
        echo 'Falar: Miauu Miauuu!';
    }
}

$cachorro = new Cachorro(5, 'Orange');
$cachorro->__str__();
$cachorro->falar();

print "\n------------------\n";

$cachorro = new Cachorro(5, 'Orange');
$cachorro->__str__();
$cachorro->falar();




?>