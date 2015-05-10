/**
 * Created by Sencer HAMARAT on 10.05.2015.
 */

jQuery(function ($) {

    if (!("WebSocket" in window)) {
        alert("Tarayıcınız Web Socket teknolojisini desteklememektedir.");
    } else {
        upstart();
    }

    function upstart() {
        var host = "ws://localhost:9090/ws";  // websocket adresi tanımı
        var socket = new WebSocket(host);  // WebSocket oluştur ve değişkene ata
        var $txt = $("#data");
        var $btnSend = $("#sendtext");

        $txt.focus();  // İmleçi Input field'a odakla


        // Düğmeye tıklandığında ya da Enter tuşuna basıldığında mesajı gönder.
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
                showServerResponse("Bağlantı kuruldu");
            };
            socket.onmessage = function (msg) {
                showServerResponse(msg.data);
            };
            socket.onclose = function () {
                //alert("connection closed....");
                showServerResponse("Bağlantı Kesildi.");
            }
        } else {
            console.log("Geçersiz Socket");
        }

        function showServerResponse(txt) {  // Mesajları HTML'e basmak için kullanılan method
            var p = document.createElement('p');
            p.innerHTML = txt;
            document.getElementById('output').appendChild(p);
        }
    }
});