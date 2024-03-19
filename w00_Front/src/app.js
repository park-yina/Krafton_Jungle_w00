// HTML ELEMENTS
const goBackBtn = document.querySelector("#goBackBtn");
const checkOthers = document.querySelector("#checkOthers");

// EVENTLISTENERS
goBackBtn.addEventListener("click", () => {
  window.location.href = "index.html";
});
checkOthers.addEventListener("click", () => {}); // 채워 넣기

// Functions
class File {
  static upload(uploaderEl) {
    uploaderEl.addEventListener("change", (event) => {
      const file = event.target.files[0];
      if (file) console.log(file.name);
    });
  }
}

const fileInput = document.querySelector("#fileInput");
fileInput.addEventListener("change", File.upload(fileInput));
