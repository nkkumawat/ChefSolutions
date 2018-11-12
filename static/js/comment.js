$("document").ready(function() {
    $("#commentForm").submit(function(e) {
        e.preventDefault();

        const token = $("[name='csrfmiddlewaretoken']").val();

        $.ajax({
            url: "/blog/addComment",
            method: "post",
            data: {
                text: $(".materialize-textarea").val(),
                customerId: $("#customerId").html(),
                recipeId: $("#recipeId").html(),
                csrfmiddlewaretoken: token
            },
            success: function(response) {
                if (response.success) {
                    console.log(response);
                    var comment = $('<li class="collection-item avatar"></li>');
                    var customerImage = $(
                        "<img src=/" +
                            $("#customerImage").html() +
                            ' alt="" class="circle">'
                    );
                    var customerName = $(
                        '<h4 class="title teal-text" style="margin-top: 0px;">' +
                            $("#customerName").html() +
                            "</h4>"
                    );
                    var commentText = $("<p>" + response.comment + "</p>");

                    comment.append(customerImage);
                    comment.append(customerName);
                    comment.append(commentText);

                    $(".collection").append(comment);

                    $(".materialize-textarea").val("");
                }
            },
            error: function(error) {
                $(".modal").modal("open");
            }
        });
    });
});
