define([
    'react',
], function(React) {
    var App = React.createClass({displayName: "App",
        getInitialState: function() {
            return {
                suggestions: []
            }
        },

        getAutoSuggestions: function(keywords) {
            /*
                @keywords - array of keywords
                Returns:
                JSON Response
            */

            var self = this;

            if (_.isArray(keywords)) {
                this._xhr = $.get('/api/complete/search?client=firefox&q=' + keywords.join('+'), function(data) {
                    self.setState({suggestions: data[1]})
                });
            }
            else {
                return false;
            }
        },

        handleChange: function(e) {
            var keywords = e.target.value.match(/\S+/g),
                self = this;

            // clear timeout if timeout is already set
            if (this._t) {
                clearTimeout(this._t);
            }

            // abort any ajax calls
            if (this._xhr) {
                this._xhr.abort();
            }

            // if no keywords then set the suggestions to empty array
            if (keywords === null) {
                this.setState({suggestions: []});
            }
            else {
                this._t = setTimeout(function() { self.getAutoSuggestions(keywords) }, 500);
            }
        },

        render: function() {
            var suggestions = [];

            _.forEach(this.state.suggestions, function(s, i) {
                suggestions.push(React.createElement("li", {key: i}, React.createElement("a", null, s)));
            })

            return (React.createElement("div", {className: "r-container"}, 
                        React.createElement("h1", null, "Google Auto Suggestion"), 
                        React.createElement("input", {autoFocus: true, autoComplete: "off", type: "text", onChange: this.handleChange, defaultValue: "", placeholder: "type something here..."}), 
                        suggestions.length > 0 ? React.createElement("ul", {className: "list"}, suggestions) : null
                    ));
        }
    });

    return App;
});
