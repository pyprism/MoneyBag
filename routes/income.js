/**
 * Created by prism on 6/25/15.
 */
var express = require('express');

var routes = function (manager) {
    var router = express.Router();

    router.route('/')
        .post(function(req, res) {
            var man = new manager.Income(req.body);
            //res.send(manager);
            console.log(man);
            console.log(req.body.income);
            res.send(req.body);
        })
        .get(function(req, res){

            var query = {};

            if(req.query.month) {
                query.month = req.query.month;
            }
            manager.Tag.find(query, function(err, name) {
                if(err)
                    res.status(500).send(err);
                else
                    res.json(name);
            });
        });

    router.route(':id')
        .get(function(req, res) {

        });

    return router;

};

module.exports = routes;