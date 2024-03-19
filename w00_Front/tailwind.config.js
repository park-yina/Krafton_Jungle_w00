/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/index.html", "./src/app.js"],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/forms")],
};
