const summaryOutput = document.getElementById("summaryOutput");
const taskOutput = document.getElementById("taskOutput");
const formOutput = document.getElementById("formOutput");

async function getActiveTab() {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  return tab;
}

function fallbackSummary(payload) {
  const sentences = payload.text.split(/[.!?]\s+/).filter(Boolean);
  const summary = sentences.slice(0, 3).join(". ");
  return summary || `This page is titled "${payload.title}" and has limited visible text.`;
}

function fallbackTasks(text) {
  const actionWords = ["apply", "submit", "review", "download", "contact", "prepare", "compare", "complete"];
  const sentences = text.split(/[.!?]\s+/).filter(Boolean);
  const tasks = sentences.filter((sentence) => actionWords.some((word) => sentence.toLowerCase().includes(word))).slice(0, 5);
  return tasks.length ? tasks : ["Review the page content", "Identify any required fields", "Confirm details before taking action"];
}

function draftForField(field) {
  const label = `${field.label} ${field.name} ${field.placeholder}`.toLowerCase();
  if (label.includes("name")) return "Demo User";
  if (label.includes("email")) return "demo@example.com";
  if (label.includes("summary") || label.includes("message")) return "Draft response for review: I am interested in learning more and can provide relevant details.";
  if (label.includes("experience")) return "Draft response for review: I have experience with Python, automation and AI-assisted workflows.";
  return "Draft response for review. Please edit before inserting.";
}

async function sendToContent(type, payload = {}) {
  const tab = await getActiveTab();
  return chrome.tabs.sendMessage(tab.id, { type, ...payload });
}

document.getElementById("analysePage").addEventListener("click", async () => {
  summaryOutput.textContent = "Analysing visible page text...";
  const payload = await sendToContent("EXTRACT_PAGE");
  summaryOutput.textContent = fallbackSummary(payload);
});

document.getElementById("buildTasks").addEventListener("click", async () => {
  taskOutput.innerHTML = "";
  const payload = await sendToContent("EXTRACT_PAGE");
  fallbackTasks(payload.text).forEach((task) => {
    const item = document.createElement("li");
    item.textContent = task;
    taskOutput.appendChild(item);
  });
});

document.getElementById("detectForms").addEventListener("click", async () => {
  formOutput.innerHTML = "<p class='status'>Looking for visible form fields...</p>";
  const payload = await sendToContent("DETECT_FORMS");
  formOutput.innerHTML = "";
  if (!payload.fields.length) {
    formOutput.innerHTML = "<p class='status'>No editable form fields were found on this page.</p>";
    return;
  }
  payload.fields.forEach((field) => {
    const card = document.createElement("div");
    card.className = "form-card";
    const label = document.createElement("label");
    label.textContent = field.label || field.name || field.selector;
    const textarea = document.createElement("textarea");
    textarea.value = draftForField(field);
    const button = document.createElement("button");
    button.type = "button";
    button.className = "secondary";
    button.textContent = "Insert reviewed text";
    button.addEventListener("click", () => {
      sendToContent("INSERT_FORM_VALUE", { selector: field.selector, value: textarea.value });
    });
    card.append(label, textarea, button);
    formOutput.appendChild(card);
  });
});
