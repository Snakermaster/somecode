//模态框居中的控制
function centerModals(){
    $('.modal').each(function(i){   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');    
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top-30);  //修正原先已经有的30个像素
    });
}


$(document).ready(function(){
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);


    $.get('/order/lorders_info/',function (data) {
        if(data.code == '200'){

            var lorder_html = template('lorder_tem_script',{orders:data.lorder_info});
            $('.orders-list').html(lorder_html);

            $(".order-accept").on("click", function(){
            var orderId = $(this).parents("li").attr("order-id");
            $(".modal-accept").attr("order-id", orderId);
            });
            $(".order-reject").on("click", function(){
            var orderId = $(this).parents("li").attr("order-id");
            $(".modal-reject").attr("order-id", orderId);

            });

            $(".order-delete").on("click", function(){
            var orderId = $(this).parents("li").attr("order-id");
            $(".modal-delete").attr("order-id", orderId);
            

            });

        $('.modal-accept').on('click',function () {
            var order_id = $('.modal-accept').attr('order-id');

            var status = 'WAIT_PAYMENT';
            $.ajax({
                url:'/order/o_status/',
                type:'PATCH',
                datatype:'json',
                data:{'order_id':order_id,'status':status},
                success:function (data) {

                    location.reload()

                }

            })
        });


        $('.modal-reject').on('click',function () {

            var order_id = $('.modal-reject').attr('order-id');
            var status = 'REJECTED';
            var comment = $('#reject-reason').val();
            $.ajax({
                url:'/order/o_status/',
                type:'PATCH',
                datatype:'json',
                data:{'order_id':order_id,'status':status,'comment':comment},
                success:function (data) {
                    location.reload()
                }
            })
        });

        }
    });
     $('.modal-delete').on('click',function () {
        var order_id = $('.modal-delete').attr('order-id');
        $.ajax({
            url:'/order/del_order',
            type:'GET',
            datatype:'json',
            data:{'order_id':order_id},
            success:function (data) {
                if(data.code=='200'){
                  location.reload()
                }
            }
        })


    });


});