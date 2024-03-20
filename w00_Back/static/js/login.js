export default class Login {
  async getToken() {
    try {
      const userId = document.querySelector("#userId").value;
      const password = document.querySelector("#password").value;
      const request = await fetch("/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          userId,
          password,
        }),
      });

      const loginData = await request.json();
      if (loginData.result === "success") {
        document.cookie = `mytoken=${loginData.token};path=/`;
        window.location.href = "/upload";
      } else {
        alert(loginData.error);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }
}
