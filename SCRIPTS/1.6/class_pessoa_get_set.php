<?php

class Pessoa {
    private $nome;
    private $idade;
    private $cpf;

    function __construct($nome, $idade, $cpf) {
        $this->nome = $nome;
        $this->idade = $idade;
        $this->cpf = $cpf;
    }

    public function getNome() {
        return $this->nome;
    }

    public function getIdade() {
        return $this->idade;
    }

    public function getCpf() {
        return $this->cpf;
    }

    public function setNome($nome) {
        $this->nome = $nome;
    }

    public function setIdade($idade) {
        $this->idade = $idade;
    }

    public function setCpf($cpf) {
        $this->cpf = $cpf;
    }

    public function __str__() {
        return "

        Nome: $this->nome
        Idade: $this->idade
        Cpf: $this->cpf";
    }

}

$pessoa = new Pessoa('Ingride', 45, 999);

echo $pessoa->__str__();

echo '
----------------------';

$pessoa->setNome('Luca');
$pessoa->setIdade(343);
$pessoa->setCpf(809809809);

echo $pessoa->__str__();