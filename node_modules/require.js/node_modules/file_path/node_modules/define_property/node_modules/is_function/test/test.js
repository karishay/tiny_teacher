var assert = require("assert"),
    isFunction = require("../src/index");


describe("isFunction", function() {
    it("should return true when the value is a Function", function() {
        assert.equal(isFunction(null), false);
        assert.equal(isFunction(undefined), false);
        assert.equal(isFunction(0), false);
        assert.equal(isFunction(""), false);
        assert.equal(isFunction({}), false);
        assert.equal(isFunction([]), false);
        assert.equal(isFunction(/./), false);

        assert.equal(isFunction(function noop() {}), true);
    });
});
