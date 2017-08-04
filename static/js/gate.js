/**
 * Created by hbot on 7/8/17.
 */
var Gate = {
    signUpValidation: function () {
        $('#sign_up').validate({
            rules: {
                'terms': {
                    required: true
                },
                'confirm': {
                    equalTo: '[name="password"]'
                }
            },
            highlight: function (input) {
                //console.log(input);
                $(input).parents('.form-line').addClass('error');
            },
            unhighlight: function (input) {
                $(input).parents('.form-line').removeClass('error');
            },
            errorPlacement: function (error, element) {
                $(element).parents('.input-group').append(error);
                $(element).parents('.form-group').append(error);
            }
        });
    },
    signInValidation: function () {
        $('#sign_in').validate({
            highlight: function (input) {
                //console.log(input);
                $(input).parents('.form-line').addClass('error');
            },
            unhighlight: function (input) {
                $(input).parents('.form-line').removeClass('error');
            },
            errorPlacement: function (error, element) {
                $(element).parents('.input-group').append(error);
            }
        });
    },
    forgotPasswordValidation: function () {
        $('#sign_in').validate({
            highlight: function (input) {
                //console.log(input);
                $(input).parents('.form-line').addClass('error');
            },
            unhighlight: function (input) {
                $(input).parents('.form-line').removeClass('error');
            },
            errorPlacement: function (error, element) {
                $(element).parents('.input-group').append(error);
            }
        });
    },
    ledgerHeadValidation: function () {
        $('#add_ledger_head').validate({
            rules: {

            },
            highlight: function (input) {
                $(input).parents('.form-line').addClass('error');
            },
            unhighlight: function (input) {
                $(input).parents('.form-line').removeClass('error');
            },
            errorPlacement: function (error, element) {
                $(element).parents('.form-group').append(error);
            }
        });
    },
    editledgerHeadValidation: function () {
        $('#edit_ledger_head').validate({
            rules: {

            },
            highlight: function (input) {
                $(input).parents('.form-line').addClass('error');
            },
            unhighlight: function (input) {
                $(input).parents('.form-line').removeClass('error');
            },
            errorPlacement: function (error, element) {
                $(element).parents('.form-group').append(error);
            }
        });
    },
    headEditHandler: function () {
        $('.btnEdit').click(function (e) {
            e.preventDefault();
            console.log('i am in fire');
            var dataId = $(this).attr('data-id');
            var ledgerCode = $(this).attr('data-ledger-code');
            var headName = $(this).siblings('p').text();

            $('#acc_head_name').val(headName);
            $('#acc_head_id').val(dataId);
            $('#acc_ledger_code').val(ledgerCode);

            $('#editHeadModal').modal('show');

        });

        $('#edit_ledger_head').submit(function (e) {
            e.preventDefault();
            var data = $(this).serialize();
            var postURL = $(this).attr('action')

            $.post(postURL,data,function(res, status){
                if(status==="success"){
                    if(res.success){
                        showNotification("bg-teal", res.message, 'top', 'right', 'animated zoomInRight', 'animated zoomOutRight');
                        $('#editHeadModal').modal('hide');
                        setTimeout(function () {
                           location.reload();

                        },2000);
                    }
                    else{
                        showNotification("bg-red", res.message, 'top', 'right', 'animated zoomInRight', 'animated zoomOutRight');
                    }
                }
                else{
                    console.log(res);
                    console.log(status);
                }

            });

        });
    }
};