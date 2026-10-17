import test from 'node:test';
import assert from 'node:assert/strict';
import { h } from '../../../valuerank/site/assets/js/dom.js';
import { createWindow } from '../helpers/fake-dom.mjs';

test('h builds an element with attributes, class, text, style, properties and children', () => {
  const { document } = createWindow();
  const child = h(document, 'i', { text: 'x' });
  const el = h(document, 'input', {
    class: 'c1 c2', id: 'i1', 'aria-label': 'L', hidden: true, disabled: false, skip: null, gone: undefined,
    style: { width: '40%' }, checked: true, value: '7',
  }, 'plain', null, false, child);
  assert.equal(el.tagName, 'INPUT');
  assert.equal(el.className, 'c1 c2');
  assert.equal(el.getAttribute('aria-label'), 'L');
  assert.equal(el.hasAttribute('hidden'), true);
  assert.equal(el.hasAttribute('disabled'), false);
  assert.equal(el.hasAttribute('skip'), false);
  assert.equal(el.style.width, '40%');
  assert.equal(el.checked, true);
  assert.equal(el.value, '7');
  assert.equal(el.textContent, 'plainx');
  const t = h(document, 'span', { text: 'hello' });
  assert.equal(t.textContent, 'hello');
});
