/**
 * Created by prism on 6/27/15.
 */
var express = require('express');

var routes = function(manager){
    var router = express.Router();

    router.route('/')
        .get(function(req, res) {
            manager.Loan.find(function(err, data){
                if(err)
                    res.status(500).send(err);
                res.json(data);
            });
        })
        .post(function(req, res) {

            var hiren = new manager.Loan(req.body);
            hiren.save(function (err) {
                if (err)
                    res.status(409).send(err);
                res.status(201).send(hiren);
            });
        });

            return router;
};

module.export = routes;