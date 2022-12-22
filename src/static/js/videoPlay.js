var playBtn = document.getElementById("play");
var icon = document.getElementById("playBtnIcon");
var video = document.getElementById("video");
var currentTime = document.getElementById("currentVidTime");
var totalTime = document.getElementById("totalVidTime");
var form = document.getElementById("form");

//Initalize Video Times
video.addEventListener("loadedmetadata", function () {
  video.currentTime = 130;
});

currentTime.innerHTML = 0;

//Call everytime video updates
video.ontimeupdate = function () {
  updateTime();
};

function updateTime() {
  var minutes = Math.floor(video.currentTime / 60);
  var seconds = Math.floor(video.currentTime - minutes * 60);
  if (seconds < 10) {
    seconds = "0" + seconds;
  }
  time = minutes + ":" + seconds + " ";

  currentTime.innerHTML = time;
}

//call after video is watched
video.onended = () => {
  form.submit();
};

//handle user input
playBtn.addEventListener("click", () => {
  if (video.paused) {
    video.play();
    icon.src = "static/assets/pause.svg";
  } else {
    video.pause();
    icon.src = "static/assets/play.svg";
  }
});
