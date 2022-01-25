let nt = document.getElementById("toggler");
let nb = document.getElementById("navs");
let ld = document.getElementById("loading-box");
let body = document.querySelector("body");
let isnt = false;
function toggleNavbar(e) {
  if (isnt) {
    e.classList.remove("fa-times");
    e.classList.add("fa-bars");
    nb.classList.remove("on");
    body.classList.remove("on");
    isnt = false;
  } else if (!isnt) {
    e.classList.add("fa-times");
    e.classList.remove("fa-bars");
    nb.classList.add("on");
    body.classList.add("on");
    isnt = true;
  }
}

window.onload = () => {
  setTimeout(() => {
    ld.classList.add("off");
    body.classList.remove("on");
  }, 750);
};

fetch('https://api.statcord.com/v3/912680688384372826')
.then(response => response.json())
.then(data => {
  document.getElementById("servercount").innerHTML = " " + String(data.data[0].servers) + " Servers";
  document.getElementById("usercount").innerHTML = " " + String(data.data[0].users) + " Users";
  document.getElementById("commandcount").innerHTML = " " + String(data.data[0].custom1) + " Votes";
})