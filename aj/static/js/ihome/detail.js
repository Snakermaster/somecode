function hrefBack() {
    history.go(-1);
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}



$(document).ready(function(){
    $(".book_house").show();
    var search_url = location.search;
    var house_id = search_url.split('=')[1];
    $.get('/house/detail/'+house_id+'/',function (data) {
        if(data.code == '200'){

             console.log(data);

        var house_html = template('house_temp_detail',{house:data.house_detail});
            $('.house_info').html(house_html);
            $('.book_house').attr('href','/house/booking/?house_id='+ house_id );
            var mySwiper = new Swiper ('.swiper-container', {
                loop: true,
                autoplay: 2000,
                autoplayDisableOnInteraction: false,
                pagination: '.swiper-pagination',
                paginationType: 'fraction'
                });


        }
    })

});