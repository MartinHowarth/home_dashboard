function startLoops() {
    // Wait until the main element has loaded.
    if (document.getElementById('main') == null) {
        var t = setTimeout(startLoops, 50);
        return;
    }
    updateClockClockWidgetModel();
}

this.onload = function(){
        startLoops();
    };
