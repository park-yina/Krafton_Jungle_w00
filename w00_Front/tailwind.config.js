/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/index.html", "./src/app.js"],
  theme: {
    extend: {
      fontFamily: {
        custom: ["Dongle", "sans-serif"],
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
