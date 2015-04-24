require.config({
	paths: {
		react: '../libs/react/react',
		jquery: '../js/libs/jquery/dist/jquery.min'
  },

	shim: {
		react: {
			exports: 'React'
		},

		jquery: {
			exports: '$'
		}
	}
});

require([
	'react',
	'components/App',
	'jquery'
	],
function(React, App) {
	React.renderComponent(App(), document.getElementById('app'));
});
