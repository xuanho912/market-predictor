import type { Metadata, Viewport } from "next";
import { PwaRegister } from "../components/pwa-register";
import "./globals.css";

export const metadata: Metadata = {
  title: "market-predictor",
  description: "Mobile display for calibrated market prediction probabilities.",
  manifest: "/manifest.json",
};

export const viewport: Viewport = {
  themeColor: "#0f766e",
  width: "device-width",
  initialScale: 1,
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <PwaRegister />
        {children}
      </body>
    </html>
  );
}
