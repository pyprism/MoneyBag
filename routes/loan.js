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

    router.route('/:loanId')
        .get(function(req, res) {

            manager.Loan.findById(req.params.loanId, function(err, data) {
                if(err)
                    res.status(500).send(err);
                else
                    res.json(data);
            });
        })
        .put(function(req, res) {

            manager.Loan.findById(req.params.loanId, function(err, data) {
                if(err)
                    res.status(500).send(err);
                else{
                    data.from = req.body.from;
                    data.to = req.body.to;
                    data.amount = req.body.amount;
                    data.date = req.body.date;
                    data.returnDate = req.body.returnDate;
                    data.active = req.body.active;
                    data.save();
                    res.json(data);
                }

            });
        });

            return router;
};

module.exports = routes;