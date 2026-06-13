import type { Metadata, Viewport } from "next";
import { PwaRegister } from "../components/pwa-register";
import "./globals.css";

const criticalDashboardCss = `
:root{color-scheme:light}*{box-sizing:border-box}body{margin:0;background:#f6f8f7;color:#14211f;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.5}button{font:inherit;color:inherit;cursor:pointer;background:transparent}svg{display:block}.mx-auto{margin-left:auto;margin-right:auto}.mt-1{margin-top:.25rem}.mt-2{margin-top:.5rem}.mt-3{margin-top:.75rem}.mt-4{margin-top:1rem}.mt-5{margin-top:1.25rem}.min-h-screen{min-height:100vh}.w-full{width:100%}.max-w-6xl{max-width:72rem}.max-w-5xl{max-width:64rem}.max-w-3xl{max-width:48rem}.px-4{padding-left:1rem;padding-right:1rem}.py-5{padding-top:1.25rem;padding-bottom:1.25rem}.p-3{padding:.75rem}.p-4{padding:1rem}.p-5{padding:1.25rem}.px-2{padding-left:.5rem;padding-right:.5rem}.px-3{padding-left:.75rem;padding-right:.75rem}.py-1{padding-top:.25rem;padding-bottom:.25rem}.py-2{padding-top:.5rem;padding-bottom:.5rem}.pb-5{padding-bottom:1.25rem}.grid{display:grid}.flex{display:flex}.block{display:block}.items-center{align-items:center}.items-start{align-items:flex-start}.justify-center{justify-content:center}.justify-between{justify-content:space-between}.flex-col{flex-direction:column}.flex-wrap{flex-wrap:wrap}.gap-2{gap:.5rem}.gap-3{gap:.75rem}.gap-4{gap:1rem}.gap-5{gap:1.25rem}.grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.rounded{border-radius:.25rem}.rounded-md{border-radius:.375rem}.rounded-lg{border-radius:.5rem}.rounded-full{border-radius:9999px}.border{border:1px solid #d8dfdc}.border-b{border-bottom:1px solid #d8dfdc}.border-line{border-color:#d8dfdc}.border-teal{border-color:#0f766e}.bg-white,.bg-panel{background:#fff}.bg-ink{background:#14211f}.bg-\\[\\#eefaf5\\]{background:#eefaf5}.text-white{color:#fff}.text-ink{color:#14211f}.text-muted{color:#66736f}.text-teal{color:#0f766e}.text-rose{color:#be123c}.text-amber{color:#b45309}.text-blue-700{color:#1d4ed8}.text-left{text-align:left}.text-right{text-align:right}.text-xs{font-size:.75rem;line-height:1rem}.text-sm{font-size:.875rem;line-height:1.25rem}.text-base{font-size:1rem;line-height:1.5rem}.text-xl{font-size:1.25rem;line-height:1.75rem}.text-2xl{font-size:1.5rem;line-height:2rem}.text-3xl{font-size:1.875rem;line-height:2.25rem}.font-medium{font-weight:500}.font-semibold{font-weight:600}.uppercase{text-transform:uppercase}.tracking-normal{letter-spacing:0}.tracking-\\[0\\.18em\\]{letter-spacing:.18em}.leading-5{line-height:1.25rem}.leading-6{line-height:1.5rem}.leading-7{line-height:1.75rem}.h-10{height:2.5rem}.w-10{width:2.5rem}.h-\\[360px\\]{height:360px}.min-w-\\[720px\\]{min-width:720px}.min-w-\\[760px\\]{min-width:760px}.overflow-x-auto{overflow-x:auto}.shadow-sm{box-shadow:0 1px 2px rgba(0,0,0,.05)}.transition{transition:color .15s,background-color .15s,border-color .15s,box-shadow .15s}.hover\\:border-teal:hover{border-color:#0f766e}.hover\\:shadow-sm:hover{box-shadow:0 1px 2px rgba(0,0,0,.05)}.space-y-1>:not([hidden])~:not([hidden]){margin-top:.25rem}.last\\:border-0:last-child{border-width:0}@media (min-width:640px){.sm\\:flex-row{flex-direction:row}.sm\\:items-start{align-items:flex-start}.sm\\:items-end{align-items:flex-end}.sm\\:justify-between{justify-content:space-between}.sm\\:text-right{text-align:right}.sm\\:grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.sm\\:grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.sm\\:grid-cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.sm\\:grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}}@media (min-width:768px){.md\\:grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.md\\:grid-cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.md\\:grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}}@media (min-width:1024px){.lg\\:grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}.lg\\:grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}.lg\\:grid-cols-\\[1\\.15fr_0\\.85fr\\]{grid-template-columns:1.15fr .85fr}.lg\\:grid-cols-\\[1\\.4fr_0\\.9fr\\]{grid-template-columns:1.4fr .9fr}}
`;

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
      <head>
        <style dangerouslySetInnerHTML={{ __html: criticalDashboardCss }} />
      </head>
      <body>
        <PwaRegister />
        {children}
      </body>
    </html>
  );
}
