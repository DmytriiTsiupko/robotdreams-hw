window.onload = function(){
  /** Ініціалізація змінної з випадковим числом друзів під час завантаження сторінки */
  let friendCount = Math.floor(Math.random() * 100);
  document.getElementById("friendCount").innerHTML = friendCount;
};

function addToFriends() {
  let btn = document.getElementById("addToFriends");
  if (btn.classList.contains("disabled")) {
    return;
  }
  let friendCount = parseInt(document.getElementById("friendCount").innerHTML);

  friendCount++;

  document.getElementById("friendCount").innerHTML = friendCount;
  btn.classList.add("disabled");
  btn.style.backgroundColor = "green"; // змінюємо колір кнопки на зелений
  btn.innerHTML = "Очікується підтвердження";
}



