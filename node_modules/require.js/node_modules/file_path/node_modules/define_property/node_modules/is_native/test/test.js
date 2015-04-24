var assert = require("assert"),
    isNative = require("../src/index");


describe("isNative", function() {
    it("should return true when the value is a native function or object", function() {
        assert.equal(isNative(function noop() {}), false);
        assert.equal(isNative(Object.prototype.hasOwnProperty), true);
    });
});
