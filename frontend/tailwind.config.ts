import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{js,ts,jsx,tsx,mdx}", "./components/**/*.{js,ts,jsx,tsx,mdx}", "./lib/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        ink: "#14211f",
        muted: "#66736f",
        panel: "#ffffff",
        line: "#d8dfdc",
        surface: "#f6f8f7",
        teal: "#0f766e",
        amber: "#b45309",
        rose: "#be123c"
      }
    }
  },
  plugins: []
};

export default config;
