
//https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript
//http://tech-blog.tomchambers.me/2016/01/13/How-to-write-a-simple-page-rewriting-Chrome-extension/

function on(id, event, fnc) {
    var el = document.getElementById(id);
    el.addEventListener(event, fnc);
}

function prepareDataToSend(data) {
    return JSON.stringify({html: data});
}

const url = 'http://127.0.0.1:5000/send';

function getHostDOM() {
    return document.body.innerHTML;
}

function sendData(data) {
    fetch(url, {
            method: "post",
            body: prepareDataToSend(data),
            headers: {
              'Content-Type': 'application/json'
            }
        })
        .then((resp) => resp.json())
        .then(resp => {
            console.log("OK:");
            chrome.tabs.getSelected(null, function(tab) {
                d = document;

                var el = document.createElement('p');

                el.innerHTML = resp.html;

                d.body.appendChild(el);
            });
        })
        .catch(error => {
            console.log("ERR: ", error);
        });
}
document.addEventListener('DOMContentLoaded', function () {
    console.log("READY!");
    on('scrapButton', 'click', function () {
        console.log('click!');
        chrome.tabs.executeScript({
            code: '(' + getHostDOM + ')();'
        }, (results) => {

            if (typeof results !== 'undefined') {
                console.log('Got DOOM data.');
                sendData(results[0]);
            } else {
                console.log('No DOOM data :C');
            }

        });

    });
});






