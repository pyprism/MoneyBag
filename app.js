/**
 * Created by prism on 6/22/15.
 */

var express = require('express'),
    mongoose = require('mongoose'),
    manager = require('./models/manager'),
    bodyParser = require('body-parser');

incomeRoute = require('./routes/income')(manager);  // injecting manager model(s) :D impressive isn't it ?
initialAmount = require('./routes/initial')(manager);
loan = require('./routes/loan')(manager);

var app = express();


app.enable('trust proxy');
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.use('/api/income',incomeRoute);
app.use('/api/initial',initialAmount);
app.use('/api/loan',loan);

var port = process.env.PORT || 4000,
    db = mongoose.connect( process.env.DB || 'mongodb://localhost/hiren_expense');


app.get('/', function(req, res){
    res.send('test');
});

app.listen(port, function(){
    console.log('App is running on port: ' + port);
});