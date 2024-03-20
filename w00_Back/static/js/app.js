import Login from "./login.js";
import File from "./file.js";

const login = new Login();

// HTML Elements
const loginBtn = document.querySelector("#loginBtn");
const fileInput = document.querySelector("#fileInput");
const rows = document.querySelectorAll(".grid");

// EventListeners
if (loginBtn) loginBtn.addEventListener("click", login.getToken);

if (fileInput) fileInput.addEventListener("change", File.upload(fileInput));

if (rows) {
  rows.forEach((row) => {
    row.addEventListener("click", async (event) => {
      let targetId = event.target.id;
      if (!targetId) {
        targetId = event.target.parentElement.parentElement.id;
      }
      const request = await fetch("/story", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          idx: targetId,
        }),
      });
      const response = await request;
      window.location.href = response.url;
    });
  });
}

// Functions
