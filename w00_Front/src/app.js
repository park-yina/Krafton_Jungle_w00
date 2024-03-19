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
