var reset = 0;
function numero(x) {
	var texto = document.querySelector(".count");
	if (reset == 0) {
		texto.innerHTML = x;
		reset = 1;
	} else {
		texto.innerHTML += x;
	}
}

function result(x) {
	var texto = document.querySelector(".count");
	texto.innerHTML = eval(texto.innerHTML);
}
