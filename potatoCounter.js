var boxes = document.querySelectorAll("td");
var count = 0;
for (var i = 0; i <boxes.length; i++) {
	var image = boxes[i].firstChild;
	if (image.src && image.src.indexOf('potato') != -1) {
		count++;
	}
}
var input = document.querySelector('[name="guess"]');
input.value = count;
var button = document.querySelector('[value="Guess!"]');
button.click()