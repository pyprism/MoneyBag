/**
 * Created by prism on 6/22/15.
 */

var express = require('express'),
    mongoose = require('mongoose'),
    manager = require('./models/manager'),
    bodyParser = require('body-parser');

incomeRoute = require('./routes/income')(manager);  // injecting manager model :D impressive isn't it ?


var app = express();


app.enable('trust proxy');
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.use('/api/income',incomeRoute);

var port = process.env.PORT || 4000,
    db = mongoose.connect( process.env.DB || 'mongodb://localhost/hiren_expense');


app.get('/', function(req, res){
    res.send('test');
});

app.listen(port, function(){
    console.log('App is running on port: ' + port);
});