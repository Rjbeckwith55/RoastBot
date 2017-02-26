// Path to python script to send urls
var pyPath = "getURL.cgi";

// Use python shell
var PythonShell = require('python-shell');
var pyshell = new PythonShell(pyPath);

// store roast
var roast;

// store urls to be tested against
var urls = [];

try{
    getPictures();
    pyshell.send(JSON.stringify(urls));
}
catch(err){
    //send bad data
    pyshell.send(JSON.stringify(-1));
}

// recieve a message from python script
pyshell.on('message', function (msg) {
    //do nothing
});

// end the input stream and allow the process to exit
pyshell.end(function (err) {
    // throw error if failed
    if (err){
        throw err;
    };
});

// Path to python script to recieve comment
pyPath = "sendComment.cgi";
pyshell = new PythonShell(pyPath);

// add all picture urls to urls array
function getPictures(){
    $.getJSON("http://www.reddit.com/r/RoastMe/top/.json?jsonp=?", function(data) { 
    $.each(data.data.children, function(i,item){
        urls.push($("<img/>").attr("src", item.data.url))
    });
});
}

// wait to recieve message from python script
function callback(msg){
    return function(){
        roast = msg
        console.log(roast);
    }
}

// execute python script and store selected reddit comment
// display roast to webpage
function getRoast() {
    // recieve a message from python script
    pyshell.on('message', function (msg) {
        // use timeout and callback to wait for message
        setTimeout(callback(msg), 100);
    });

    // end the input stream and allow the process to exit
    pyshell.end(function (err) {
        // throw error if failed
        if (err){
            throw err;
        };
    });
}

getRoast();