/**
 * Created by Sencer HAMARAT on 10.05.2015.
 */

jQuery(function ($) {

    if (!("WebSocket" in window)) {
        alert("Your browser does not supporting Web Socket technology.");
    } else {
        upstart();
    }

    function upstart() {
        var host = "ws://localhost:9090/ws";  // websocket address definition
        var socket = new WebSocket(host);  // Create a WebSocket
        var $txt = $("#data");
        var $btnSend = $("#sendtext");

        $txt.focus();  // Focus cursot to input


        // Send message if Return pressed or button clicked.
        $btnSend.on('click', function () {
            var text = $txt.val();
            if (text == "") {
                return;
            }
            socket.send(text);
            $txt.val("");
        });

        $txt.keypress(function (evt) {
            if (evt.which == 13) {
                $btnSend.click();
            }
        });

        if (socket) {
            socket.onopen = function () {
                showServerResponse("Connection Established.");
            };
            socket.onmessage = function (msg) {
                showServerResponse(msg.data);
            };
            socket.onclose = function () {
                showServerResponse("Connection Closed.");
            }
        } else {
            console.log("Invalid Socket");
        }

        function showServerResponse(txt) {  // Put messages to HTML dynamically
            var p = document.createElement('p');
            p.innerHTML = txt;
            document.getElementById('output').appendChild(p);
        }
    }
});
