/**
 * Created by prism on 6/23/15.
 */

var mongoose = require('mongoose'),
    Schema = mongoose.Schema;

var initialStatusSchema = new Schema({
    amount: {
        type: Number,
        default: 0
    }
});

var incomeSchema = new Schema({
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
    createdOn: {
        type: Date,
        default: Date.now()
    },
    month: String,
    year: Number
});

var expenseSchema = new Schema({
    source: [{
        type: Schema.Types.ObjectId,
        ref: 'Tag'
    }],
    expense: {
        type: Number,
        default: 0
    },
    createdOn: {
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

exports.Tag = mongoose.model('Tag', tagSchema);
exports.Income = mongoose.model('Income', incomeSchema);
exports.Expense = mongoose.model('Expense', expenseSchema);
exports.Loan = mongoose.model('Loan', loanSchema);
exports.Initial = mongoose.model('InitialAmount', initialStatusSchema);