var assert = require("assert"),
    isObjectLike = require("../src/index");


describe("isObjectLike", function() {
    it("should return true when the value is like an Object", function() {
        assert.equal(isObjectLike(null), false);
        assert.equal(isObjectLike(undefined), false);
        assert.equal(isObjectLike(0), false);
        assert.equal(isObjectLike(""), false);
        assert.equal(isObjectLike(function noop() {}), false);
        assert.equal(isObjectLike(/./), true);
        assert.equal(isObjectLike({}), true);
        assert.equal(isObjectLike([]), true);
    });
});
