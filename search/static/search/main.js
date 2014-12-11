// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
 
/*
The functions below will create a header with csrftoken
*/
 
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
 
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


// Submit post on submit
$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});

// AJAX for posting
function create_post() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "/search/", // the endpoint
        type : "POST", // http method
        data : { the_post : $('#search').val(), vegetarian : $('#vegetarian').is(':checked') , vegan : $('#vegan').is(':checked'), glutenfree : $('#gluten-free').is(':checked'), soyfree : $('#soy-free').is(':checked'), dairyfree : $('#dairy-free').is(':checked'), searchtype : $('#searchtype').val()}, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#search').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            $("#recipe").html(''); //clear the previous thing searched 
            var index, index2;
            
            //This formats the results with the HTML for viewing the recipe
            for (index = 0; index < json.recipe_names.length; ++index) {
                $("#recipe").append("<div class = \"row\" id=\"first-row"+index+"\">");
                $("#first-row"+index).append("<div class= \"col-md-11\" id= \"inside-recipe"+index+"\">");
                
                $("#inside-recipe"+index).append(json.recipe_names[index]+"<br/>");
                
                $("#first-row"+index).append("</div>");
                $("#first-row"+index).append("<div class= \"col-md-1\" id= \"recipe-glyph"+index+"\">");

                //add to menu
                $("#recipe-glyph"+index).append("<a class=\"btn btn-default\" href='/menu/"+json.recipe_ids[index]+"/yourmenu/'><span class=\"glyphicon glyphicon-plus\"></span></a>");

                
                $("#first-row"+index).append("</div>");
                $("#recipe").append("</div>");

                $("#recipe").append("<div class = \"row\" id= \"second-row"+index+"\">");
                $("#second-row"+index).append("<div class= \"col-md-4\" id= \"inside-ingredient"+index+"\">");
                
                $("#inside-ingredient"+index).append("<h4>Ingredients</h4>");
                for (index2 = 0; index2 < json.recipe_ing[index].length; ++index2) {
                    $("#inside-ingredient"+index).append(json.recipe_ing[index][index2]+"<br/>");
                }
                $("#inside-ingredient"+index).append("<p/>");

                $("#second-row"+index).append("</div><div class= \"col-md-4\" id= \"inside-instruction"+index+"\">");
                
                $("#inside-instruction"+index).append("<h4>Instructions</h4>");
                for (index2 = 0; index2 < json.recipe_inst[index].length; ++index2) {
                    $("#inside-instruction"+index).append(json.recipe_inst[index][index2]+"<br/>");
                }
                
                $("#second-row"+index).append("</div>");
                $("#recipe").append("</div>");



            }
            //show/hides a recipe
            $( "[id^='first-row']" ).click(function() {
                var index = this.id.slice(9);
                var secondrow= "second-row".concat(index);
                $( '[id="'+secondrow+'"]' ).slideToggle();
            });
            
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

