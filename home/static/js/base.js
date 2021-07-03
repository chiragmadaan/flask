//console.log("Hello from the other side");

// const button = document.getElementById("id");
// const button2 = document.querySelector(".class #id");

// button.addEventListener('click', function() {
// 	console.log("You clicked on button");
// })
// el.classList.add('classname');
// setTimeout(function() {el.classList.remove('classname')}, 2000);
// setTimeout(() => el.classList.remove('classname'), 2000);
//
//$(document).ready(function(){
//  console.log("Hello from inside");
//    $("#login-form").on("submit", function(event){
//        console.log("login form submitted 1")
////        event.preventDefault();
//
//        var formValues= $(this).serialize();
//        console.log(formValues)
////        $.post("process_form.php", formValues, function(data){
////            // Display the returned data in browser
////            $("#result").html(data);
////        });
////        event.stopPropagation();
//    });
//});

var option = {
    animation : true,
    delay : 3000
  }

  function ShowToast(p1 = "No heading", p2 = "No body"){
    document.getElementById("toastHeader").innerHTML = p1;
    document.getElementById("toastBody").innerHTML = p2;
    var toastHTMLElement = document.getElementById("toast");
    var toastElement = new bootstrap.Toast( toastHTMLElement, option );
    toastElement.show();
  }

  function ClearToasts(){
    var toast = document.getElementById("toast");
    var toasts = document.getElementById("toasts");
    toasts.innerHTML = toast.outerHTML;
  }

  function GenerateToast(p1 = "No heading", p2 = "No body"){
  console.log(`showing ${p2}`)
    document.getElementById("toastHeader").innerHTML = p1;
    document.getElementById("toastBody").innerHTML = p2;
    var toast = document.getElementById("toast");
    var toasts = document.getElementById("toasts");
    toasts.innerHTML = toasts.innerHTML + toast.outerHTML;
//<!--        var toastElList = document.querySelectorAll('.toast')-->
//<!--        new bootstrap.Toast(toastElList[toastElList.length-1], option).show()-->
  }

  function ShowAllToasts(){
    var toastElList = [].slice.call(document.querySelectorAll('.toast'))
    toastElList[0].remove()
    toastElList = [].slice.call(document.querySelectorAll('.toast'))
    var toastList = toastElList.map(function (toastEl) {
      return new bootstrap.Toast(toastEl, option)
    })
    toastList.forEach((el) => el.show());

  }