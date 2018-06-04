const path = require("path");

const ExtractTextPlugin = require('extract-text-webpack-plugin');

exports.devServer = ({ host, port } = {}) => ({

  devServer: {
    // Display only errors to reduce the amount of output.
    stats: "errors-only",

    // Parse host and port from env to allow customization.
    //
    // If you use Docker, Vagrant or Cloud9, set
    // host: options.host || "0.0.0.0";
    //
    // 0.0.0.0 is available to all network devices
    // unlike default `localhost`.
    // host: process.env.HOST, // Defaults to `localhost`
    // port: process.env.PORT, // Defaults to 8080
    open: true, // Open the page in browser
    overlay: true,
  },

});

// JS
exports.loadJS = ({ include, exclude } = {}) => ({
  module: {
    rules: [
      {
        test: '/\.js$/',
        include,
        exclude,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['env'],
          }
        },
      },
    ],
  }
});

// CSS
exports.loadCSS = ({ include, exclude } = {}) => ({
  module: {
    rules: [
      {
        test: /\.scss$/,
        include,
        exclude,
        loader: ExtractTextPlugin.extract(['css-loader', 'sass-loader']),
      },
    ]
  },
});
