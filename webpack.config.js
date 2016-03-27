var debug = process.env.NODE_ENV !== "production",
    webpack = require('webpack');

module.exports = {
    context: __dirname + "/public/src",
    devtool: debug ? "inline-sourcemap" : null,
    entry: "./js/client.js",
    module: {
        loaders: [
            {
                test: /\.js?$/,
                exclude: /(node_modules)/,
                loader: 'babel-loader',
                query: {
                    presets: ['react', 'es2015', 'stage-0'],
                    plugins: ['transform-class-properties', "react-html-attrs", "transform-decorators-legacy"]
                }
            }
        ]
    },
    output: {
        path: __dirname + "/static/",
        filename: "client.min.js"
    },
    plugins: debug ? [] : [
        new webpack.optimize.DedupePlugin(),
        new webpack.optimize.OccurenceOrderPlugin(),
        new webpack.optimize.UglifyJsPlugin({ mangle: false, sourcemap: false})
    ]
};
