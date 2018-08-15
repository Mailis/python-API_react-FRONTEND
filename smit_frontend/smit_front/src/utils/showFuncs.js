/*jshint esversion: 6 */
export function showError(err){
    if(err){
        var element = document.getElementById("error");
        if(element){
            element.innerHTML = err;
            element.classList.add("feeback_isvisible");
        }
    }
}
export function showRichError(err, message){
    var messageElement = document.createElement("div");
    messageElement.classList.add("error_precision");
     // and give it some content 
    var newContent = document.createTextNode(message); 
    // add the text node to the newly created div
    messageElement.appendChild(newContent); 
    if(err){
        var element = document.getElementById("error");
        if(element){
            element.innerHTML = err;
            element.prepend(messageElement);
            element.classList.add("feeback_isvisible");
        }
    }
}

export function showSuccess(response, message = ''){
    //console.log("SUCC MESSAGE response" , message, response);
    if(response || message){
        var element = document.getElementById("success");
        if(element){
            var resp = "";
            if(response.statusText){
                resp = (response.statusText.toLowerCase() !== "no content")? response.statusText : "";
            }
            element.innerHTML = message + " " +    resp;
            element.classList.add("feeback_isvisible");

            setTimeout(function(){
            element.classList.remove("feeback_isvisible");
            }, 5000);
        }
    }
}


export function flashMessage(message, elementId){
    var element = document.getElementById(elementId);
    if(element){
        element.innerHTML = message;
        element.classList.add("show");
    
        setTimeout(function(){
        element.classList.remove("show");
        }, 5000);
    }
}


export function showElement(elementId, removeHidingClassName){
    var element = document.getElementById(elementId);
    element.classList.remove(removeHidingClassName);
}


export function toggleElementById(elemId, hideClassName){
    //console.log(' toggleElementById(elemId, hideClassName)', elemId );
    var element = document.getElementById(elemId);
    //console.log(' toggleElementById(elemId, hideClassName)', element );
    if(element){
        if(element.classList.contains( hideClassName )){
            element.classList.remove(hideClassName);
        }
        else{
            element.classList.add(hideClassName);
        }
    }
}