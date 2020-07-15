'use strict';
var HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    output: {
        filename: "build.js"
    },
    plugins: [
        new HtmlWebpackPlugin({
            title: "WebmStock",
            hash: true
        })
   ]
}
