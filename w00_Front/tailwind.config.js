/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/*.html", "./src/*.js"],
  theme: {
    extend: {
      fontFamily: {
        custom: ["Dongle", "sans-serif"],
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
