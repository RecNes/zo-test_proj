/**
 * Created by sencer on 07.05.2015.
 */
$(document).ready(function () {

    var ws;

    var host_input = $("#host");
    var port_input = $("#port");
    var uri_input = $("#uri");
    var message_box = $("#message_box");


    function doSock() {
        // Get values else use defaults
        var host = ((host_input.val()) ? host_input.val() : "localhost");
        var port = ((port_input.val()) ? port_input.val() : "8888");
        var uri = ((uri_input.val()) ? uri_input.val() : "/ws");

        ws = new WebSocket("ws://" + host + ":" + port + uri);  // Socket instance'ı oluştur.

        ws.onmessage = function (evt) {
            message_box.html("Message: " + evt.data);
//            alert("message received: " + evt.data)
        };

        ws.onclose = function (evt) {
            message_box.html("Connection closed");
//            alert("Connection close");
        };

        ws.onopen = function (evt) {
            message_box.html("Connection opened");
//            $("#host").css("background", "#00ff00");
//            $("#port").css("background", "#00ff00");
//            $("#uri").css("background", "#00ff00");
        };
    }

    doSock(); // first self run

    $("#open").click(function (evt) {
        evt.preventDefault();
        doSock();
    });
});