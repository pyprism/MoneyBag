/**
 * Created by hbot on 7/8/17.
 */
$(function () {
    //Tooltip
    $('[data-toggle="tooltip"]').tooltip({
        container: 'body'
    });

    //Popover
    $('[data-toggle="popover"]').popover();
})
//On focus event
$('.form-control').focus(function () {
    $(this).parent().addClass('focused');
});

//On focusout event
$('.form-control').focusout(function () {
    var $this = $(this);
    if ($this.parents('.form-group').hasClass('form-float')) {
        if ($this.val() == '') { $this.parents('.form-line').removeClass('focused'); }
    }
    else {
        $this.parents('.form-line').removeClass('focused');
    }
});

//On label click
$('body').on('click', '.form-float .form-line .form-label', function () {
    $(this).parent().find('input').focus();
});

//Not blank form
$('.form-control').each(function () {
    if ($(this).val() !== '') {
        $(this).parents('.form-line').addClass('focused');
    }
});


    //Datetimepicker plugin
    $('.datetimepicker').bootstrapMaterialDatePicker({
        format: 'YYYY-MM-DD HH:mm',
        weekStart: 1
    });

    $('.datepicker').bootstrapMaterialDatePicker({
        format: 'YYYY-MM-DD',
        weekStart: 1,
        time: false,
        currentDate: new Date()
    });
    $('.datepicker2').bootstrapMaterialDatePicker({
        format: 'YYYY-MM-DD',
        weekStart: 1,
        time: false,
    });
    $('.datepicker3').bootstrapMaterialDatePicker({
        format: 'YYYY-MM',
        time:false,
        monthPicker:true,
    });
    $('.timepicker').bootstrapMaterialDatePicker({
        format: 'HH:mm',
        date: false
    });

//notifications
function showNotification(colorName, text, placementFrom, placementAlign, animateEnter, animateExit) {
    if (colorName === null || colorName === '') { colorName = 'bg-black'; }
    if (text === null || text === '') { text = 'Turning standard Bootstrap alerts'; }
    if (animateEnter === null || animateEnter === '') { animateEnter = 'animated fadeInDown'; }
    if (animateExit === null || animateExit === '') { animateExit = 'animated fadeOutUp'; }
    var allowDismiss = true;

    $.notify({
        message: text
    },
        {
            type: colorName,
            allow_dismiss: allowDismiss,
            newest_on_top: true,
            timer: 1000,
            placement: {
                from: placementFrom,
                align: placementAlign
            },
            animate: {
                enter: animateEnter,
                exit: animateExit
            },
            template: '<div data-notify="container" class="bootstrap-notify-container alert alert-dismissible {0} ' + (allowDismiss ? "p-r-35" : "") + '" role="alert">' +
            '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
            '<span data-notify="icon"></span> ' +
            '<span data-notify="title">{1}</span> ' +
            '<span data-notify="message">{2}</span>' +
            '<div class="progress" data-notify="progressbar">' +
            '<div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
            '</div>' +
            '<a href="{3}" target="{4}" data-notify="url"></a>' +
            '</div>'
        });
}

//select2
 $(".myselect").select2();
//print page
$('.btnPrint').click(function () {
   window.print();
});
