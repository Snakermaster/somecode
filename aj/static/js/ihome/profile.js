function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;

}




$(document).ready(function () {
    // var avatar = $('#user-avatar').val();
    // var s = '<img id="user-avatar" src="/static/media/'+ avatar +'">';
    // $('#avater_show').html(s);
    $.get('/user/my_info/',function (data) {
        if(data.code.code =='200'){

        $('#user-avatar').attr('src','/static/media/'+data.user_info.avatar)

        }


    });



    $('#form-avatar').submit(function (e) {
    e.preventDefault();
        $(this).ajaxSubmit({
            url:'/user/profile/',
            type:'PATCH',
            datatype:'json',
            success:function (data) {
                if(data.code.code =='200'){

                    $('#user-avatar').attr('src','/static/media/' + data.img_avatar);


                }
            }


        });


    })
});
$(document).ready(function () {

    $('#form-name').submit(function (e) {
            e.preventDefault();

            var username = $('#user-name').val();
            $.ajax({
                url:'/user/profile_name/',
                data:{'username':username},
                type:'PATCH',
                datatype:'json',
                success:function (data) {
                    if(data.code =='200'){

                      alert('保存成功')
                    }else if(data.code == '1011'){
                        $('.error-msg').html(data.msg);
                        $('.error-msg').show()


                    }
                }

                })

        })

});















