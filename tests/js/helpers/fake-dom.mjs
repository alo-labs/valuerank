// Minimal DOM for driving the site's DOM modules in Node. Supports the element tree,
// attributes/dataset/classList, simple selectors (tag, #id, .class, [attr], [attr="v"]
// compounds joined by commas; no combinators), events, and a fake window.

const kebab = (s) => s.replace(/[A-Z]/g, (c) => `-${c.toLowerCase()}`);

class TextNode {
  constructor(text) { this.nodeType = 3; this.textContent = String(text); this.parentNode = null; }
}

function parseCompound(src) {
  const spec = { tag: null, id: null, classes: [], attrs: [] };
  const re = /([a-zA-Z][\w-]*)|#([\w-]+)|\.([\w-]+)|\[([\w:-]+)(?:=(?:"([^"]*)"|([^\]]*)))?\]/y;
  let m;
  let pos = 0;
  while (pos < src.length) {
    re.lastIndex = pos;
    m = re.exec(src);
    if (!m) throw new Error(`fake-dom: unsupported selector "${src}"`);
    if (m[1]) spec.tag = m[1].toUpperCase();
    else if (m[2]) spec.id = m[2];
    else if (m[3]) spec.classes.push(m[3]);
    else spec.attrs.push([m[4], m[5] ?? m[6] ?? null]);
    pos = re.lastIndex;
  }
  return spec;
}

const LIST_API = new Set(['length', 'forEach', 'item', 'entries', 'keys', 'values', Symbol.iterator]);

/** A live-NodeList stand-in: indexable, iterable, forEach; deliberately no map/filter/find (a real NodeList has none). */
export function nodeList(items) {
  return new Proxy(items, {
    get(target, key) {
      if (key === 'item') return (i) => target[i] ?? null;
      if (typeof key === 'symbol' || LIST_API.has(key) || /^\d+$/.test(key)) {
        const value = Reflect.get(target, key);
        return typeof value === 'function' ? value.bind(target) : value;
      }
      return undefined;
    },
  });
}

export class FakeElement {
  constructor(tagName, doc) {
    this.tagName = tagName.toUpperCase();
    this.ownerDocument = doc;
    this.attributes = {};
    this.childNodes = [];
    this.parentNode = null;
    this.listeners = {};
    this.style = {};
    this.checked = false;
    this._value = undefined;
    this.focused = false;
    this.clicks = 0;
    const el = this;
    this.dataset = new Proxy({}, {
      get: (_t, k) => el.attributes[`data-${kebab(k)}`],
      set: (_t, k, v) => { el.attributes[`data-${kebab(k)}`] = String(v); return true; },
    });
    this.classList = {
      add: (...c) => { const s = new Set(el.className.split(/\s+/).filter(Boolean)); c.forEach((x) => s.add(x)); el.className = [...s].join(' '); },
      remove: (...c) => { el.className = el.className.split(/\s+/).filter((x) => x && !c.includes(x)).join(' '); },
      contains: (c) => el.className.split(/\s+/).includes(c),
      toggle: (c, force) => {
        const on = force === undefined ? !el.classList.contains(c) : force;
        el.classList[on ? 'add' : 'remove'](c);
        return on;
      },
    };
  }

  get id() { return this.attributes.id ?? ''; }
  set id(v) { this.attributes.id = String(v); }
  get className() { return this.attributes.class ?? ''; }
  set className(v) { this.attributes.class = String(v); }
  get hidden() { return 'hidden' in this.attributes; }
  set hidden(v) { if (v) this.attributes.hidden = ''; else delete this.attributes.hidden; }
  get children() { return nodeList(this.childNodes.filter((n) => n.nodeType !== 3)); }
  get firstChild() { return this.childNodes[0] ?? null; }
  get value() { return this._value ?? this.attributes.value ?? ''; }
  set value(v) { this._value = String(v); }
  get type() { return this.attributes.type ?? ''; }
  get name() { return this.attributes.name ?? ''; }
  get href() { return this.attributes.href ?? ''; }
  set href(v) { this.attributes.href = String(v); }
  get download() { return this.attributes.download ?? ''; }
  set download(v) { this.attributes.download = String(v); }

  get textContent() { return this.childNodes.map((n) => n.textContent).join(''); }
  set textContent(v) { this.replaceChildren(String(v)); }
  get innerHTML() { return this.textContent; }

  setAttribute(k, v) { this.attributes[k] = String(v); }
  getAttribute(k) { return k in this.attributes ? this.attributes[k] : null; }
  hasAttribute(k) { return k in this.attributes; }
  removeAttribute(k) { delete this.attributes[k]; }

  appendChild(node) {
    node.parentNode = this;
    this.childNodes.push(node);
    return node;
  }
  append(...nodes) {
    nodes.forEach((n) => this.appendChild(typeof n === 'string' ? new TextNode(n) : n));
  }
  replaceChildren(...nodes) {
    this.childNodes.forEach((n) => { n.parentNode = null; });
    this.childNodes = [];
    this.append(...nodes);
  }
  contains(node) {
    for (let n = node; n; n = n.parentNode) if (n === this) return true;
    return false;
  }

  matchesCompound(src) {
    const s = parseCompound(src);
    if (s.tag && this.tagName !== s.tag) return false;
    if (s.id && this.id !== s.id) return false;
    if (!s.classes.every((c) => this.classList.contains(c))) return false;
    return s.attrs.every(([k, v]) => (v === null ? this.hasAttribute(k) : this.getAttribute(k) === v));
  }
  matches(selector) {
    return selector.split(',').some((part) => {
      const chain = part.trim().split(/\s+/);
      if (!this.matchesCompound(chain.pop())) return false;
      let node = this.parentNode;
      while (chain.length && node) {
        if (node.matchesCompound && node.matchesCompound(chain.at(-1))) chain.pop();
        node = node.parentNode;
      }
      return chain.length === 0;
    });
  }
  querySelectorAll(selector) {
    const out = [];
    const walk = (node) => node.children.forEach((c) => { if (c.matches(selector)) out.push(c); walk(c); });
    walk(this);
    return nodeList(out);
  }
  querySelector(selector) { return this.querySelectorAll(selector)[0] ?? null; }

  addEventListener(type, fn) { (this.listeners[type] ??= []).push(fn); }
  dispatchEvent(event) {
    event.target ??= this;
    event.defaultPrevented ??= false;
    event.preventDefault ??= () => { event.defaultPrevented = true; };
    (this.listeners[event.type] || []).forEach((fn) => fn(event));
    return !event.defaultPrevented;
  }
  /** Test helper: dispatch a simple event with extra properties. */
  fire(type, props = {}) {
    const event = { type, ...props };
    this.dispatchEvent(event);
    return event;
  }
  click() { this.clicks += 1; this.fire('click'); }
  focus() { this.focused = true; this.ownerDocument.activeElement = this; }
}

export function createDocument(bodyHtmlBuilder) {
  const doc = {
    activeElement: null,
    listeners: {},
    createElement: (tag) => new FakeElement(tag, doc),
    createTextNode: (t) => new TextNode(t),
    getElementById: (id) => doc.documentElement.querySelector(`#${id}`),
    querySelector: (s) => doc.documentElement.querySelector(s),
    querySelectorAll: (s) => doc.documentElement.querySelectorAll(s),
    addEventListener: (t, fn) => { (doc.listeners[t] ??= []).push(fn); },
    dispatchEvent: (ev) => { ev.target ??= doc; (doc.listeners[ev.type] || []).forEach((fn) => fn(ev)); },
    fire(type, props = {}) { doc.dispatchEvent({ type, ...props }); },
  };
  doc.documentElement = new FakeElement('html', doc);
  doc.body = new FakeElement('body', doc);
  doc.documentElement.appendChild(doc.body);
  if (bodyHtmlBuilder) bodyHtmlBuilder(doc);
  return doc;
}

/** Build elements quickly: add(parent, 'button', {id, 'aria-expanded': 'false', text}) */
export function add(parent, tag, attrs = {}, ...kids) {
  const el = parent.ownerDocument.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === 'text') el.textContent = v;
    else if (k === 'checked') el.checked = v;
    else if (k === 'value') el.value = v;
    else el.setAttribute(k, v);
  }
  el.append(...kids);
  parent.appendChild(el);
  return el;
}

export function createWindow({ search = '', pathname = '/rankings/', stored = {}, dark = false, storageThrows = false } = {}) {
  const document = createDocument();
  const store = new Map(Object.entries(stored));
  const win = {
    document,
    location: { search, pathname },
    history: {
      calls: [],
      replaceState(state, title, url) {
        win.history.calls.push(url);
        win.location.search = url.includes('?') ? url.slice(url.indexOf('?')) : '';
      },
    },
    localStorage: {
      writes: [],
      getItem(k) { if (storageThrows) throw new Error('denied'); return store.has(k) ? store.get(k) : null; },
      setItem(k, v) { if (storageThrows) throw new Error('denied'); win.localStorage.writes.push(k); store.set(k, String(v)); },
    },
    matchMedia: (query) => ({ matches: dark && query.includes('dark'), media: query }),
    URL: {
      created: [], revoked: [],
      createObjectURL(blob) { const u = `blob:fake-${win.URL.created.length}`; win.URL.created.push({ url: u, blob }); return u; },
      revokeObjectURL(u) { win.URL.revoked.push(u); },
    },
    Blob: class FakeBlob { constructor(parts, opts) { this.parts = parts; this.type = opts.type; } text() { return this.parts.join(''); } },
    CustomEvent: class FakeCustomEvent { constructor(type, init = {}) { this.type = type; this.detail = init.detail; } },
  };
  return win;
}
