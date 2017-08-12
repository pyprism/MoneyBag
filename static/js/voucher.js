/**
 * Created by hbot on 8/11/17.
 */
var Voucher={
    payment_method_table:{},
    payment_method_table_count:0,
    init:function(){

        Voucher.payment_method_table=jQuery('#payment_method_table').DataTable({
            "paging":   false,
            "info":     false,
            "ordering": false,
            "bFilter": false

        });

        jQuery('#payment_method_table tbody').on( 'click', '.icon-delete', function () {
            Voucher.payment_method_table
                .row( $(this).parents('tr') )
                .remove()
                .draw();

            Voucher.paymentMethodTotalRecalculate()
        });


    },
    addMorePaymentMethod:function()
    {
        Voucher.payment_method_table_count=Voucher.payment_method_table_count+1;

        Voucher.payment_method_table.row.add([
            '<select name="payment_methods[]" class="form-control select2_me_sc'+Voucher.payment_method_table_count+'"></select>',
            '<input step="any" min="0" type="number" name="payment_method_amount[]" placeholder="amount " class="form-control pamount scu'+Voucher.payment_method_table_count+'" value="0">',
            '<textarea name="payment_method_note[]" placeholder="notes" class="form-control scup'+Voucher.payment_method_table_count+'"></textarea>',
            '<button type="button" class="btn btn-danger pull-right icon-delete">X</button>'
        ]).draw(false);
        // console.log(PAYMENT_METHOD_LIST);
        jQuery('.select2_me_sc'+Voucher.payment_method_table_count).select2({data :PAYMENT_METHOD_LIST});

        // jQuery('.select2_me_sc'+Voucher.payment_method_table_count).vall(PAYMENT_METHOD_LIST[0].id).trigger('change.select2');

        Voucher.paymentMethodTotalRecalculate()

        jQuery(document).on("change", ".scu"+Voucher.payment_method_table_count, function() {
            Voucher.paymentMethodTotalRecalculate()
        });

    },
    paymentMethodTotalRecalculate:function()
    {
        var sum = 0;
        $(".pamount").each(function(){
            sum += +$(this).val();
        });
        jQuery('.payment_method_table_summation').text(sum);
    }
}