/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Poppins", "sans-serif"],
      },
      gridTemplateColumns: {
        "70/30": "70% 28%",
      },
      colors: {
        primary: "#3b82f6",
        "primary-light": "#38bdf8",
        "primary-extra-light": "#e0f2fe",
        "primary-dark": "#0284c7",
        "primary-extra-dark": "#0369a1",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
