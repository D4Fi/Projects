function add() {
	var texto = document.querySelector(".count");
	texto.innerHTML = parseFloat(texto.innerHTML) + 1;
}

function reset() {
	var texto = document.querySelector(".count");
	texto.innerHTML = "0";
}

function sub() {
	var texto = document.querySelector(".count");
	texto.innerHTML = parseFloat(texto.innerHTML) - 1;
}
