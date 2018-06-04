const path = require("path");
const merge = require("webpack-merge");
const ExtractTextPlugin = require('extract-text-webpack-plugin');

const parts = require("./webpack.parts");

const commonConfig = merge([

  {
    entry: ['./website/static/js/index.js', './website/static/css/main.scss'],
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

  parts.loadJS({ include: path.resolve('./website/static/js/')}),

  parts.loadCSS(),

]);

const productionConfig = merge([]);

const developmentConfig = merge([
  parts.devServer({
    // Customize host/port here if needed
    // host: process.env.HOST,
    // port: process.env.PORT,
  }),
]);

module.exports = mode => {

  if (mode === "production") {
    return merge(commonConfig, productionConfig, { mode });
  }

  return merge(commonConfig, developmentConfig, { mode });
};