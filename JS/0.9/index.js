function soma() {
	var numero = document.querySelector('.number');
	var valor = document.querySelector(".number").innerHTML;
	string = parseInt(valor) + 1
	numero.innerHTML = string;
}

function diminuir() {
	var numero = document.querySelector('.number');
	var valor = document.querySelector(".number").innerHTML;
	string = parseInt(valor) - 1
	numero.innerHTML = string;
}
