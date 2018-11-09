$(document).ready(function() {
    var product1 = $("#product1").html();
    var product2 = $("#product2").html();
    var product3 = $("#product3").html();
    
    $('#productImage1').css('backgroundImage', 'url(/'+ product1 +')');
    $('#productImage2').css('backgroundImage', 'url(/'+ product2 +')');
    $('#productImage3').css('backgroundImage', 'url(/'+ product3 +')');

    $('.productImage').click(function(e){
        var no = e.target.id.substr(-1);
        console.log(no);
        switch(no){
            case '1':
                $('#productShow').attr('src', '/'+ product1 +'');
                break;
            case '2':
                $('#productShow').attr('src', '/'+ product2 +'');
                break;
            case '3':
                $('#productShow').attr('src', '/'+ product3 +'');
                break;
        }
        
    });

    console.log(product1, product2, product3);
});
