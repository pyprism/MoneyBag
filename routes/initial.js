/**
 * Created by prism on 6/26/15.
 */
var express = require('express');

var routes = function(manager) {
  var router = express.Router();

    router.route('/')
        .get(function(req, res) {
            manager.Initial.find(function(err, amount){
                if(err)
                    res.status(500).send(err);
                res.json(amount);
            });
        })
        .post(function(req, res) {
           manager.Initial.find(function(err, amount) {
               if (amount.length !== 0) {
                   var message = { "status": "already exists"};
                   res.status(200).json(message);
               }
               else {
                   var init = new manager.Initial(req.body);
                   init.save();

                   res.status(201).send(init);
               }
           })
        });
    return router;
};

module.exports = routes;