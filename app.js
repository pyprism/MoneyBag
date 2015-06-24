/**
 * Created by prism on 6/22/15.
 */

var express = require('express'),
    mongoose = require('mongoose'),
    manager = require('./models/manager');

var app = express(),
    router = express.Router();

var port = process.env.PORT || 4000,
    db = mongoose.connect( process.env.DB || 'mongodb://localhost/hiren_expense');


router.route('/expense')
    .get(function(req, res){
       manager.Tag.find(function(err, name) {
           if(err)
                res.status(500).send(err);
           else
               res.json(name);
       });
    });

app.enable('trust proxy');
app.use('/api',router);

app.get('/', function(req, res){
    res.send('test');
});

app.listen(port, function(){
    console.log('App is running on port: ' + port);
});