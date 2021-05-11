const POST_URL = "http://127.0.0.1:5000/answer_attempt";
let gameOver = false;
$("#game_form").on("submit", async (e) => {
	e.preventDefault();
	if (!gameOver) {
		let attempt = e.target[0].value;
		let response = await axios.post(POST_URL, { attempt });
		let value = response.data.result;
		let message = document.createElement("span");
		let responseDisplay = $("#response-display");
		let score = $("#score");
		responseDisplay.empty();
		message.innerText = value;
		if (value == "ok") {
			message.className = "success";
			score.html(parseInt(score.html()) + attempt.length);
		} else {
			message.className = "fail";
		}
		responseDisplay.append(message);
	} else {
		alert("Sorry your time ended!");
	}
});

let count = 60;
let clock = $("#clock");
clock.html(count);

let timer = setInterval(function () {
	count--;
	clock.html(count);
	if (count == 0) {
		clearInterval(timer);
		clock.html("Time's Up.");
		clock.className = "fail";
		gameOver = true;
	}
}, 1000);
