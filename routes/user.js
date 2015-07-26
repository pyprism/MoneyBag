/**
 * Created by prism on 7/21/15.
 */
var express = require('express');



var routes = function(userObj, createJWT) {
    var router = express.Router();

    router.route('/signup')
        .post(function( req, res) {
            userObj.User.findOne({email: req.body.email }, function(err, existingUser) {
                if (existingUser) {
                    return res.status(409).json({ "message": "Email is already taken"});
                }

                var user = new userObj.User({
                    email: req.body.email,
                    password: req.body.password
                });
                user.save(function() {
                    res.json({ "token": createJWT(user)});
                });
            });
        });

    router.route('/login')
        .post(function(req, res) {
            userObj.User.findOne({ email: req.body.email }, '+password', function(err, user) {
                if (!user) {
                    return res.status(401).json({ 'message': 'Wrong email and/or password'})
                }

                user.comparePassword(req.body.password, function(err, isMatch) {
                    if(!isMatch) {
                        return res.status(401).json({ 'message': 'Wrong email or/and password'});
                    }
                    res.json({ 'token': createJWT(user)});
                });
            });

        });

    return router;
};

module.exports = routes;