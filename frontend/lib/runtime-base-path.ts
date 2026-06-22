"use client";

const configuredBasePath = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export function getRuntimeBasePath(): string {
  if (typeof window === "undefined") {
    return normalizeBasePath(configuredBasePath);
  }

  const configured = normalizeBasePath(configuredBasePath);
  const pathname = window.location.pathname;
  if (configured && (pathname === configured || pathname.startsWith(`${configured}/`))) {
    return configured;
  }

  const firstSegment = pathname.split("/").filter(Boolean)[0];
  if (!firstSegment || firstSegment.includes(".")) {
    return "";
  }

  return `/${firstSegment}`;
}

function normalizeBasePath(value: string): string {
  const trimmed = value.trim();
  if (!trimmed || trimmed === "/") {
    return "";
  }
  return trimmed.startsWith("/") ? trimmed : `/${trimmed}`;
}
