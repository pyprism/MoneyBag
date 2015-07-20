/**
 * Created by prism on 7/20/15.
 */
var mongoose = require('mongoose'),
    bcrypt = require('bcryptjs'),
    Schema = mongoose.Schema;



var userSchema = new Schema({
    email: { type: String, lowercase: true},
    password: {type: String, select: false}
});

userSchema.pre('save', function(next) {
   var user = this;
    if(!user.isModified('password')) {
        return next();
    }

    bcrypt.genSalt(10, function(err, salt) {
        bcrypt.hash(user.password, salt, function(err, hash) {
            user.password = hash;
            next();
        });
    });
});