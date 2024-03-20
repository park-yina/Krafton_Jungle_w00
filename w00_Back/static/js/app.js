import Login from "./login.js";
import File from "./file.js";

const login = new Login();

// HTML Elements
const loginBtn = document.querySelector("#loginBtn");
const fileInput = document.querySelector("#fileInput");

// EventListeners
if (loginBtn) loginBtn.addEventListener("click", login.getToken);
if (fileInput) fileInput.addEventListener("change", File.upload(fileInput));

// Functions
