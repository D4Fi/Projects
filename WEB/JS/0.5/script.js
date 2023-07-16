
function mudarCor() {
	var listColor = ["red",  "blue", "green", "gray"]
	var color = document.querySelector(".container")
	color.style.background = listColor[Math.floor(Math.random() * 10)]

}
