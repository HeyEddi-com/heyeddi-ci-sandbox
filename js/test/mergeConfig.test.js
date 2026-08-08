import test from 'node:test';
import assert from 'node:assert/strict';
import { mergeConfig } from '../src/mergeConfig.js';

test('mergeConfig returns nested upper', () => {
  const out = mergeConfig({ nested: { value: 'ok' } }, { flag: true });
  assert.equal(out, 'OK');
});
