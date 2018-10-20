$("document").ready(function() {
    $(".modal").modal();
    $(".addToCart").click(function(e) {
        const id = e.target.id;
        const quantity = $("#quantity" + id).val();
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
                    $(".modal-content>h4").html("product added successfully");
                    $(".modal-content>p").html(
                        res.added_count + " total product in your cart"
                    );
                    $(".modal").modal("open");
                } else {
                    $(".modal-content>h4").html(
                        "Error in adding the product to the cart"
                    );
                    $(".modal").modal("open");
                    console.log("no");
                }
            }
        });
    });
});
