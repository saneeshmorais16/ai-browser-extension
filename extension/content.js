function isVisible(element) {
  const style = window.getComputedStyle(element);
  const rect = element.getBoundingClientRect();
  return style.display !== "none" && style.visibility !== "hidden" && rect.width > 0 && rect.height > 0;
}

function extractVisibleText() {
  const ignored = new Set(["SCRIPT", "STYLE", "NOSCRIPT", "SVG"]);
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      const parent = node.parentElement;
      if (!parent || ignored.has(parent.tagName) || !isVisible(parent)) {
        return NodeFilter.FILTER_REJECT;
      }
      return node.textContent.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
    }
  });
  const chunks = [];
  while (walker.nextNode()) {
    chunks.push(walker.currentNode.textContent.trim());
  }
  return chunks.join(" ").replace(/\s+/g, " ").slice(0, 8000);
}

function labelForField(field) {
  if (field.id) {
    const label = document.querySelector(`label[for="${CSS.escape(field.id)}"]`);
    if (label) return label.textContent.trim();
  }
  const wrapperLabel = field.closest("label");
  return wrapperLabel ? wrapperLabel.textContent.trim() : "";
}

function selectorForField(field, index) {
  if (field.id) return `#${CSS.escape(field.id)}`;
  if (field.name) return `[name="${CSS.escape(field.name)}"]`;
  field.dataset.aiAssistantIndex = String(index);
  return `[data-ai-assistant-index="${index}"]`;
}

function detectFormFields() {
  return [...document.querySelectorAll("input:not([type=hidden]):not([type=password]), textarea")]
    .filter((field) => !field.disabled && !field.readOnly && isVisible(field))
    .map((field, index) => ({
      selector: selectorForField(field, index),
      name: field.getAttribute("name") || "",
      placeholder: field.getAttribute("placeholder") || "",
      label: labelForField(field),
      type: field.getAttribute("type") || field.tagName.toLowerCase()
    }));
}

chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (message.type === "EXTRACT_PAGE") {
    sendResponse({ title: document.title, url: location.href, text: extractVisibleText() });
    return true;
  }
  if (message.type === "DETECT_FORMS") {
    sendResponse({ fields: detectFormFields() });
    return true;
  }
  if (message.type === "INSERT_FORM_VALUE") {
    const field = document.querySelector(message.selector);
    if (field && "value" in field) {
      field.value = message.value;
      field.dispatchEvent(new Event("input", { bubbles: true }));
      sendResponse({ inserted: true });
    } else {
      sendResponse({ inserted: false });
    }
    return true;
  }
});
