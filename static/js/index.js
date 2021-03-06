 var socket;
$(document).ready(function() {
console.log('http://' + document.domain + ':' + location.port)
    socket = io();
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });
    socket.on('message', function(msg) {
        $('#res').html(library.json.prettyPrint(JSON.parse(msg)));
    });
});

if (!library)
   var library = {};

library.json = {
   replacer: function(match, pIndent, pKey, pVal, pEnd) {
      var key = '<span class=json-key>';
      var val = '<span class=json-value>';
      var str = '<span class=json-string>';
      var r = pIndent || '';
      if (pKey)
         r = r + key + pKey.replace(/[": ]/g, '') + '</span>: ';
      if (pVal)
         r = r + (pVal[0] == '"' ? str : val) + pVal + '</span>';
      return r + (pEnd || '');
      },
   prettyPrint: function(obj) {
      var jsonLine = /^( *)("[\w]+": )?("[^"]*"|[\w.+-]*)?([,[{])?$/mg;
      return JSON.stringify(obj, null, 3)
         .replace(/&/g, '&amp;').replace(/\\"/g, '&quot;')
         .replace(/</g, '&lt;').replace(/>/g, '&gt;')
         .replace(jsonLine, library.json.replacer);
      }
   };

function Submit() {
    var text = document.getElementById("text_json").value
     $.ajax({
        type: "POST",
        url: "/productionplan",
        dataType: "json",
        contentType: 'application/json',
        data: text,
        success: function (msg) {
           // $('#res').html(library.json.prettyPrint(msg));
        },
    });
}
