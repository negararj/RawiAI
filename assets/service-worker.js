const CACHE_NAME = "rawiai-demo-v2";
const APP_SHELL = ["/", "/manifest.webmanifest", "/rawiai-icon.svg"];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(APP_SHELL))
  );
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    Promise.all([
      self.clients.claim(),
      // Drop any cache left over from an earlier version of this worker -
      // otherwise a device that installed the PWA before a code change
      // can keep serving a stale app shell indefinitely.
      caches.keys().then((keys) =>
        Promise.all(keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key)))
      ),
    ])
  );
});

self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") {
    return;
  }

  // Page navigations must always hit the network fresh. A plain fetch()
  // here can still be answered from the browser's own HTTP cache even
  // though this handler is "network first" - that stale index.html would
  // keep pointing at JS bundle files a new deploy no longer serves.
  if (event.request.mode === "navigate") {
    event.respondWith(
      fetch(event.request, { cache: "no-store" }).catch(() => caches.match(event.request))
    );
    return;
  }

  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request))
  );
});
