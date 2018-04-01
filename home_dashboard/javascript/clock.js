var clockTimeElementID = 'clockTime';
var clockDateElementID = 'clockDate';

function startClock() {
    // Wait until the clock element has loaded.
    if (document.getElementById(clockTimeElementID) == null) {
        var t = setTimeout(startClock, 50);
        return;
    }
    var today = new Date();
    var day = today.getDate();
    var month = today.toLocaleString('en-gb', { month: "long" });
    var year = today.getFullYear();
    var hours = today.getHours();
    var minutes = today.getMinutes();
    var seconds = today.getSeconds();
    minutes = padInt(minutes);
    seconds = padInt(seconds);
    document.getElementById(clockTimeElementID).innerHTML = hours + ":" + minutes + ":" + seconds;
    document.getElementById(clockDateElementID).innerHTML = day + " " + month + " " + year;
    var t = setTimeout(startClock, 500);
}

function padInt(i) {
    // add zero in front of numbers < 10
    if (i < 10) {i = "0" + i};
    return i;
}
