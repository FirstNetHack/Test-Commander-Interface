$(document).ready(function(){
    console.log("yes");
    $('.checkbox').change(function() {
        console.log("yes");
        if (this.checked) {
            var current_var = $("progress").attr("value")
            $('progress').val(current_var + 33.33);
        } else {
            var current_var = $("progress").attr("value")
            $('progress').val(current_var - 33.33);
        }

        if ($("progress").attr("value") == 99.99) {
            alert("All floors cleared!");
        }
    });

    $.get("demo_test.asp", function("10.1.103.116/8000", status){
        alert("Data: " + data + "\nStatus: " + status);
    });
})
