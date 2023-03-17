document.addEventListener("click", function(event) {
  if (event.clientX > 300 && event.clientX < 350 && event.clientY > 100 && event.clientY < 200) {
    document.getElementById("easter-egg").style.display = "block";
  }
});

document.addEventListener("dblclick", function(event) {
  var selectedText = window.getSelection().toString();
  if (selectedText === "Seat") {
    document.getElementById("easter-egg").style.display = "block";
  }
});

document.addEventListener("click", function(event) {
  var selectedText = window.getSelection().toString();
  if (selectedText === "CLOSE") {
    document.getElementById("easter-egg").style.display = "none";
  }
});


