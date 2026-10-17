// Tiny element builder shared by the DOM modules (no globals; the document is passed in).
const PROPS = ['checked', 'value'];

export function h(doc, tag, attrs = {}, ...children) {
  const el = doc.createElement(tag);
  for (const [key, val] of Object.entries(attrs)) {
    if (val === null || val === undefined || val === false) continue;
    if (key === 'class') el.className = val;
    else if (key === 'text') el.textContent = val;
    else if (key === 'style') Object.assign(el.style, val);
    else if (PROPS.includes(key)) el[key] = val;
    else el.setAttribute(key, val === true ? '' : String(val));
  }
  el.append(...children.filter((c) => c !== null && c !== undefined && c !== false));
  return el;
}
