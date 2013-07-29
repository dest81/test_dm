$(document).ready(function () {

    $('.select li').on("click", function(event){
        $.ajax({
            url: "/",
            data: "model=" + $(this).attr('role'),
            success: function(html){
                $("#results").html(html);
            }
        });
    });
});