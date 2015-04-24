require.config({
	paths: {
		react: '../libs/react/react',
		jquery: '../js/libs/jquery/dist/jquery-2.0.2.min'
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
