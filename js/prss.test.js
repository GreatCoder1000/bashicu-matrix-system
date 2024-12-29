const assert = require('assert');
const PrSS = require('./prss.js');

describe('PrSS', function () {
  it('should initialize with valid sequences', function () {
    const validSequences = [
      [], [0], [0, 1], [0, 1, 1], [0, 1, 2, 3, 4, 5]
    ];
    validSequences.forEach(seq => {
      const prss = new PrSS(seq);
      assert.deepStrictEqual(prss.sequence, seq);
    });
  });

  it('should throw error for invalid types', function () {
    assert.throws(() => new PrSS(123), TypeError);
    assert.throws(() => new PrSS(['a', 'b', 'c']), TypeError);
  });

  it('should throw error for invalid values', function () {
    const invalidSequences = [
      [1], [0, 2], [0, 1, 3]
    ];
    invalidSequences.forEach(seq => {
      assert.throws(() => new PrSS(seq), Error);
    });
  });

  it('should return correct string representation', function () {
    const prss = new PrSS([0, 1, 2]);
    assert.strictEqual(prss.toString(), '(0)(1)(2)');
  });

  it('should evaluate sequences correctly', function () {
    let prss = new PrSS([0, 1, 2, 3]);
    assert.deepStrictEqual(prss.eval().sequence, [0, 1, 2, 2, 2, 2]);

    prss = new PrSS([0, 1, 2, 3, 4, 1]);
    assert.deepStrictEqual(prss.eval().sequence, [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]);

    prss = new PrSS([0, 1]);
    assert.deepStrictEqual(prss.eval().sequence, [0, 0, 0, 0]);
  });

  it('should throw error for evaluating empty sequence', function () {
    const prss = new PrSS([]);
    assert.throws(() => prss.eval(), Error);
  });
});
