function add_To_Cart(good_id){

    // var csrf = $('input[name="csrfmiddlewaretoken"]').val()

    $.ajax({
        url:'/home/add_To_Cart/',
        type:'POST',
        // hearders:{'X-CSRFToken':csrf},
        dataType:'json',
        data:{'good_id':good_id},
        success : function(data) {
            if (data.code == '200') {
                goods_count()
                console.log(data.msg)
                console.log(data.data.c_num)
                $('#num_' + good_id).html(data.data.c_num)
            }
            else{

                alert(data.msg)
            }

        },
        error:function () {

            alert('请求失败')


            }

    })
}

function desc_To_Cart(goods_id) {

    $.ajax({
        url:'/home/desc_To_Cart/',
        type:'POST',
        datatype:'json',
        data:{'goods_id':goods_id},
        success:function(data) {

            if( data.data.c_num == '0'){
                // 方法1强刷整个页面
                // location.reload()
                // 方法2删除个数为0的整整个li标签
                goods_count()
                $('#cart_' + goods_id).remove()

            }else{
                if (data.code =='200'){
            console.log(data.msg)
            console.log(data.data.c_num)

            $('#num_'+goods_id).html(data.data.c_num)
                }else {
                    alert(data.msg)

                }

            }
        },error:function() {
            alert('请求失败')
        }
    })
}



$.get('/home/refresh_goods/', function(data) {
    if(data.code == '200'){
        for(var i=0;i<data.data.length;i+=1){
            $('#num_'+data.data[i][0]).html(data.data[i][1])

                }
            }
    else{
        // alert(data.msg)
    }
        });

function change_cart_goods(goods_id) {

    $.ajax({
        url:'/home/change_cart_goods/',
        type:'POST',
        datatype:'json',
        data:{'goods_id':goods_id},
        success:function (data) {
            if (data.code == '200'){
                goods_count()
                if(data.is_select){
                    $('#cart_goods_select_'+goods_id).html('√')

                }else{
                    $('#cart_goods_select_'+goods_id).html(' ')
                }if(data.all_select){
                    $('#all_select').html('√')
                }else{
                    $('#all_select').html('')
                }
        }


    }})

}


function goods_count(){
    $.get('/home/goods_count/', function(data){
        if(data.code == '200'){
            $('#goods_money').html('总价：'+ data.data)
        }
    })
}
goods_count()


function all_select_goods(i){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/home/change_all_cart_goods/',
        type:'POST',
        data:{'all_select': i},
        dataType:'json',
        headers:{'X-CSRFToken':csrf},
        success:function(data){
            goods_count()
            if(i == '1'){
                s = '<span  style="height:30px;" id="all_select" onclick="all_select_goods(0)">√</span>'
            }else{
                s= '<span  style="height:30px;" id="all_select" onclick="all_select_goods(1)"></span>'
            }
            $('#change_all_select').html(s)
            for(var j=0; j<data.all_goods_id.length;j++){
                if( i == '1'){
                     $('#cart_goods_select_' + data.all_goods_id[j]).html('√')
                }else{
                    $('#cart_goods_select_' + data.all_goods_id[j]).html('')
                }
            }
        }
    })
}












