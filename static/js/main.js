var x = document.getElementById("dbtn");
var y = document.getElementById("sbtn");
    
var z = document.getElementById("panbtn");

$( document ).ready(function() {


    
    x.style.display = "none";
    
    y.style.display = "none";

    z.style.display = "none";

});
//  var xmlhttp;
// xmlhttp=new XMLHttpRequest();

//     // -----switch-----

// $("#AllOnoff").click(function() {
//   $('input:checkbox').not(this).prop('checked', this.checked);
//   //  window.alert('All Light: ' + $(this).prop('checked'));


  
   
//  });

//  $(function() {
//     $('#s1').change(function() {
//       window.alert('Light 1: ' + $(this).prop('checked'));
//     })
//   });
//   $(function() {
//     $('#s2').change(function() {
//       window.alert('Light 2: ' + $(this).prop('checked'));
//     })
//   });

//   $(function() {
//     $('#s3').change(function() {
//       window.alert('Light 3: ' + $(this).prop('checked'));
//     })
//   });

//  $(function() {
//     $('#s4').change(function() {
//       window.alert('Light 4: ' + $(this).prop('checked'));
//     })
//   });
//   $(function() {
//     $('#s5').change(function() {
//       window.alert('Light 5: ' + $(this).prop('checked'));
//     })
//   });

//   $(function() {
//     $('#s6').change(function() {
//       window.alert('Light 6: ' + $(this).prop('checked'));
//     })
//   });

//   $(function() {
//     $('#s7').change(function() {
//       window.alert('Light 7: ' + $(this).prop('checked'));
//     })
//   });

//   $(function() {
//     $('#s8').change(function() {
//       window.alert('Light 8: ' + $(this).prop('checked'));
//     })
//   });

// btn function
  
    
function drivebtn() {

 document.getElementById("dbtn");

  if (document.getElementById("dbtn").style.display === "none") {
    document.getElementById("dbtn").style.display = "block";
  } else {
    document.getElementById("dbtn").style.display = "none";
  }
}

    
function switchbtn() {

var y = document.getElementById("sbtn");

if (y.style.display === "none") {
  y.style.display = "block";
} else {
  y.style.display = "none";
}
}

 function lift(button) {
 

   
     if (z.value == "down") {

      
        
       $(button).html($('<i/>',{class:'fas fa-caret-square-up'}));
         z.value="up"

      }
      else {
       $(button).html($('<i/>',{class:'fas fa-caret-square-down'}));
       z.value="down"
 
      }

      if ($(button).text().trim() == 'Show') {
        $(button).html($('<i/>',{class:' 	fas fa-caret-square-up'}));

       }
      else {
       $(button).html($('<i/>',{class:'fas fa-caret-square-down'})).append(' Show');
 
      }

}






// // ----Remote drive----




// function forward() {
//   var check= "check"

//   window.alert(check)

// }
// function left() {

// xmlhttp.open("GET","img/RAKSHAK LOGO S 2.png",true);
// xmlhttp.send();

// }

// function right() {

// xmlhttp.open("GET","img/RAKSHAK LOGO S 2.png",true);
// xmlhttp.send();

// }

// function backward() {

// xmlhttp.open("GET","img/RAKSHAK LOGO S 2.png",true);
// xmlhttp.send();

// }

//input mask bundle ip address
// var ipv4_address = $('#ipv4');
// ipv4_address.inputmask({
//     alias: "ip",
//     greedy: false //The initial mask shown will be "" instead of "-____".
// });

// // device toggle
// $('#devices').change(function () {
//     const dip = $(this).val();


   
    
// });

