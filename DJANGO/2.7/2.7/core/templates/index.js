document.querySelector('#room-name-input').focus();
document.querySelector('#room-name-input').onkeyup = function(e) {
	
	if( e.key === 'Enter') {
		document.querySelector('#room-name-submit').click();
	}
};

document.querySelector('#room-name-submit').onclick = function(e) {
	var roomName = document.querySelector('#room-name-input').value;
	window.location.pathname = '/chat/' + roomName + '/';
};
