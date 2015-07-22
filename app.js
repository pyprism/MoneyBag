/**
 * Created by prism on 6/22/15.
 */

var express = require('express'),
    mongoose = require('mongoose'),
    manager = require('./models/manager'),
    user = require('./models/users'),
    bodyParser = require('body-parser'),
    jwt = require('jwt-simple'),
    moment = require('moment');

incomeRoute = require('./routes/income')(manager);  // injecting manager model(s) :D impressive isn't it ?
initialAmount = require('./routes/initial')(manager);
loan = require('./routes/loan')(manager);

var app = express();

/*
 |--------------------------------------------------------------------------
 | Login Required Middleware
 |--------------------------------------------------------------------------
 */
function ensureAuthenticated(req, res, next) {
    if (!req.headers.authorization) {
        return res.status(401).send({ message: 'Please make sure your request has an Authorization header' });
    }
    var token = req.headers.authorization.split(' ')[1];

    var payload = null;
    try {
        payload = jwt.decode(token, "some secret strings ? ;) , what about Hiren ? :P hehe ");
    }
    catch (err) {
        return res.status(401).send({ message: err.message });
    }

    if (payload.exp <= moment().unix()) {
        return res.status(401).send({ message: 'Token has expired' });
    }
    req.user = payload.sub;
    next();
}


app.enable('trust proxy');
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.use('/api/income',incomeRoute);
app.use('/api/initial',initialAmount);
app.use('/api/loan',loan);

var port = process.env.PORT || 4000,
    db = mongoose.connect( process.env.DB || 'mongodb://localhost/hiren_expense'),
    TOKEN_SECRET = process.env.TOKEN_SECRET || 'A hard to guess string';


app.get('/', function(req, res){
    res.send('test');
});

app.listen(port, function(){
    console.log('App is running on port: ' + port);
});