// Minimal DOM stand-ins for the chart mount and loader tests.
export class FakeElement {
  constructor(attrs = {}, children = []) {
    this.attrs = { ...attrs };
    this.children = children;
    this.listeners = {};
    this.textContent = '';
    this.hidden = false;
    this.parentNode = null;
    children.forEach((child) => { child.parentNode = this; });
  }
  get dataset() { return new Proxy({}, { get: (_, key) => this.attrs[`data-${key.replace(/[A-Z]/g, (c) => `-${c.toLowerCase()}`)}`] }); }
  focus() { this.focused = true; }
  setAttribute(name, value) { this.attrs[name] = String(value); }
  getAttribute(name) { return name in this.attrs ? this.attrs[name] : null; }
  addEventListener(type, fn) { (this.listeners[type] ??= []).push(fn); }
  removeEventListener(type, fn) { this.listeners[type] = (this.listeners[type] ?? []).filter((f) => f !== fn); }
  dispatch(type, detail, extra = {}) { (this.listeners[type] ?? []).slice().forEach((fn) => fn({ type, detail, target: this, preventDefault() {}, ...extra })); }
  walk() { return this.children.flatMap((c) => [c, ...c.walk()]); }
  matches(selector) {
    const m = /^\[([\w-]+)(?:="([^"]*)")?\]$/.exec(selector);
    if (!m) throw new Error(`unsupported selector ${selector}`);
    return m[1] in this.attrs && (m[2] === undefined || this.attrs[m[1]] === m[2]);
  }
  querySelectorAll(selector) { return this.walk().filter((el) => el.matches(selector)); }
  querySelector(selector) { return this.querySelectorAll(selector)[0] ?? null; }
}

export function createObserverFactory() {
  const created = [];
  const factory = (callback) => {
    const observer = { callback, observed: [], disconnected: false, observe(el) { this.observed.push(el); }, disconnect() { this.disconnected = true; } };
    created.push(observer);
    return observer;
  };
  factory.created = created;
  factory.show = (el) => created.forEach((o) => o.callback([{ target: el, isIntersecting: true }]));
  factory.hide = (el) => created.forEach((o) => o.callback([{ target: el, isIntersecting: false }]));
  return factory;
}

export function createFakeDocument({ plotly } = {}) {
  const appended = [];
  const doc = {
    defaultView: { Plotly: plotly },
    appended,
    head: { appendChild: (el) => appended.push(el) },
    createElement: (tag) => ({ tag }),
  };
  return doc;
}
