"use client";

import { useEffect } from "react";
import { getRuntimeBasePath } from "../lib/runtime-base-path";

export function PwaRegister() {
  useEffect(() => {
    if ("serviceWorker" in navigator) {
      const basePath = getRuntimeBasePath();
      const swPath = `${basePath}/sw.js`;
      navigator.serviceWorker.register(swPath, { scope: basePath ? `${basePath}/` : "/" }).catch(() => undefined);
    }
  }, []);

  return null;
}
