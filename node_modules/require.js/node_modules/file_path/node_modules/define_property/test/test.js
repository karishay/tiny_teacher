var assert = require("assert"),
    defineProperty = require("../src/index");


describe("defineProperty(object, name, value)", function() {
    it("should add define property on object", function() {
        var person = {};

        defineProperty(person, "name", {
            value: "Bob"
        });

        assert.equal(person.name, "Bob");
    });
});
