const backendUrl = document.getElementById("backendUrl");
const saveStatus = document.getElementById("saveStatus");

chrome.storage.sync.get(["backendUrl"], (items) => {
  backendUrl.value = items.backendUrl || "http://localhost:8000";
});

document.getElementById("saveOptions").addEventListener("click", () => {
  chrome.storage.sync.set({ backendUrl: backendUrl.value.trim() }, () => {
    saveStatus.textContent = "Saved.";
  });
});
