  $(function() {
      //var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    var socket = io();


    var username = null;

    var wrapper = $("#live-chat-alert").parent("div.clearfix")
    $("#live-chat-username-button").click(function() {
        if(wrapper.hasClass( "alert" )){
            wrapper.removeClass("alert alert-warning");
            $( "#live-chat-alert" ).html("");
         }
      //console.log(event)
     //event.preventDefault();
     if ($("#username-input").val() == ''){
        wrapper.addClass("alert alert-warning");
        $( "#live-chat-alert" ).html("No username entered");
     }else{


          console.log("hi button stuff");

          username = $("#username-input").val();
            console.log("client emit");
         socket.emit("sendusername", username);
         //io.serverSideEmit('sendusername', {'username': username} );
         //io.emit('sendusername', {'username': username} );


     }
       socket.on("comfirmusername", (usernamestatus) => {
       console.log("working on client side");
          if (usernamestatus == true){
            $( "#live-chat-username" ).addClass( "hide" );
            $( "#live-chat-message" ).removeClass( "hide" );
          }else{
            wrapper.addClass("alert alert-warning");
            $( "#live-chat-alert" ).html("Username already taken");
          }
        });

    });


});