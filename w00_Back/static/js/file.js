export default class File {
  static upload(uploaderEl) {
    uploaderEl.addEventListener("change", async (event) => {
      const file = event.target.files[0];
      if (file) {
        const formData = new FormData();
        formData.append("file", file);
        try {
          const token = document.cookie;
          const response = await fetch("/upload", {
            method: "POST",
            headers: {
              Authorization: `Bearer ${token}`,
            },
            body: formData,
          });
          if (response.status !== 200) {
            throw new Error();
          }

          // 이지선다
          window.location.href = response.url;
          // window.location.replace(response.url);
        } catch (error) {
          console.error("Uploading Error: ", error);
        }
      }
    });
  }
}
