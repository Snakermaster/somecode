function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}
$(document).ready(function () {
    $('#form-auth').submit(function (e) {
        e.preventDefault();
        $('#real-name').focus(function () {
            $('.error-msg').hide()
        });
        $('#id-card').focus(function () {
            $('.error-msg').hide()
        });


        var real_name = $('#real-name').val();
        var id_card = $('#id-card').val();
        $.ajax({
            url:'/user/auth/',
            datatype:'json',
            type:'PATCH',
            data:{'real_name':real_name,'id_card':id_card},
            success:function (data) {
                console.log(data)
                if(data.code == '1012' | data.code =='1013'){
                $('.error-msg').html(data.msg);
                $('.error-msg').show()
                }if(data.code == '200'){

                    $('.btn-success').hide()

                }
            }


        })
    });
    $.get('/user/auth_info/',function (data) {

        if(data.code.code == '200'){

            $('#real-name').val(data.user_info.id_name);
            $('#id-card').val(data.user_info.id_card);
            if(data.user_info.id_card){

                $('.btn-success').hide()
            }
        }


    })
})
