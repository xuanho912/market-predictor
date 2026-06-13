"use client";

import { useEffect } from "react";

const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export function PwaRegister() {
  useEffect(() => {
    if ("serviceWorker" in navigator) {
      const swPath = `${basePath}/sw.js`;
      navigator.serviceWorker.register(swPath, { scope: `${basePath || "/"}` }).catch(() => undefined);
    }
  }, []);

  return null;
}
