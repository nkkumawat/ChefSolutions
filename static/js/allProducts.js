$("document").ready(function() {
    $(".modal").modal();

    $(".addtoCart-modal").click(function (e) {
        const id = e.target.id;
        const quantity = $("#quantity").val();
        const token = $("[name='csrfmiddlewaretoken']").val();
        $.ajax({
            url: "/cart/add",
            method: "post",
            data: {
                quantity: quantity,
                product_id: id,
                csrfmiddlewaretoken: token
            },
            success: function(res) {
                if (res.success) {
                    $("#quantity").val(1);
                      M.toast({html: 'Product added to Cart'});
                } else {
                     M.toast({html: "Error in adding the product to the cart"});
                }
            }
        });
    });

    $(".addToCart").click(function(e) {
        $(".modal").modal("open");
        $(".modal-content>h5").html(e.target.name);
        $(".modal-footer>div>div>a").attr("id" , e.target.id);
    });
});
