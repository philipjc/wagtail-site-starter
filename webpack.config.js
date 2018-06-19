const path = require("path");
const merge = require("webpack-merge");
const ExtractTextPlugin = require('extract-text-webpack-plugin');

const parts = require("./webpack.parts");

const commonConfig = merge([

  {
    entry: ['./assets/js/index.js', './assets/css/main.scss'],
  },

  {
    output: {
      path: path.resolve('./website/static/dist/'),
      filename: "[name].js",
    }
  },

  {
    plugins: [
      new ExtractTextPlugin({
        filename: './css/[name].css',
        allChunks: true,
      })
    ],
  },

  parts.loadJS({ include: path.resolve('./assets/js/')}),

  parts.loadCSS(),

]);

const productionConfig = merge([

  parts.minifyJavaScript(),

  parts.minifyCSS({
    options: {
      discardComments: {
        removeAll: true,
      },
      // Run cssnano in safe mode to avoid
      // potentially unsafe transformations.
      safe: true,
    },
  }),

]);

const developmentConfig = merge([

  parts.devServer({
    // Customize host/port here if needed
    // host: process.env.HOST,
    // port: process.env.PORT,
  }),

    parts.generateSourceMaps({ type: 'source-map' }),

]);

module.exports = mode => {

  if (mode === "production") {
    return merge(commonConfig, productionConfig, { mode });
  }

  return merge(commonConfig, developmentConfig, { mode });
};