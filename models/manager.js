/**
 * Created by prism on 6/23/15.
 */

var mongoose = require('mongoose'),
    Schema = mongoose.Schema();

var initialStatusSchema = new Schema({
    amount: {
        type: Number,
        default: 0
    }
});

var managerSchema = new Schema({
    income: {
        type: Number,
        default: 0
    },
    source: [{
        type: Schema.Types.ObjectId,
        ref: 'Tag'
    }],
    expense: {
        type: Number,
        default: 0
    },
    createdAt: {
        type: Date,
        default: Date.now()
    },
    month: String,
    year: Number
});

var tagSchema = new Schema ({
    name: String
});

var loanSchema = new Schema ({
    from: String,
    to: String,
    amount: Number,
    date: Date,
    active: {
        type: Boolean,
        default: true
    }
});


module.exports = mongoose.model('Tag', tagSchema);
module.exports = mongoose.model('Manager', managerSchema);
module.exports = mongoose.model('Loan', loanSchema);
module.exports = mongoose.model('InitialAmount', initialStatusSchema);