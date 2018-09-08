$(document).ready(function(){
    $(".auth-warn").show();
});
function centerModals(){
    $('.modal').each(function(i){   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top-30);  //修正原先已经有的30个像素
    });
}


$(document).ready(function () {
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);

    $.get('/house/house_info/',function (data) {

        if(data.code =='200'){
            $('.auth-warn').hide();
            $('#houses-list').show();
            for(var i = 0;i<data.house_info.length;i+=1){
               var house_str = '<li house-id="'+data.house_info[i].id +'"><a href="/house/detail/?house_id='+data.house_info[i].id+'"><div class="house-title">';
                house_str += '<b>房屋ID:'+data.house_info[i].id+'—'+'房屋标题：'+data.house_info[i].title+'</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
                house_str += '<button type="button" class="btn btn-danger house-delete" data-toggle="modal" data-target="#delete-modal">删除</button>';
                house_str += '</div><div class="house-content">';
                house_str += '<img alt="" src="/static/media/'+ data.house_info[i].image+'">';
                house_str += '<div class="house-text"><ul><li>位于：';
                house_str += data.house_info[i].area +'</li><li>价格：￥';
                house_str += data.house_info[i].price+'/晚</li><li>发布时间：';
                house_str += data.house_info[i].create_time;
                house_str += '</li></ul></div></div></a></li>';
                $('#houses-list').append(house_str);
            }
            $(".house-delete").on("click", function(e){
                e.preventDefault();
                var houseId = $(this).parents("li").attr("house-id");
                $(".modal-delete").attr("house-id", houseId);

            });

        }else if(data.code =='1014'){
            $('.auth-warn').show();
            $('#houses-list').hide();
        }
    });
    $('.modal-delete').on('click',function () {
        var house_id = $('.modal-delete').attr('house-id');
        $.ajax({
            url:'/house/del_house/',
            datatype:'json',
            type:'GET',
            data:{'house_id':house_id},
            success:function (data) {
                if(data.code=='200'){
                    location.reload()
                }

            }


        })


    })


});

