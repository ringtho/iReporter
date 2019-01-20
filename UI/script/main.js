 $(document).ready(function(){
        $("#btn2").click(function(){
        confirm("Are you sure you want to delete this record?!");
        $(".grid1").remove();

          });
        });

$(document).ready(function(){
    $("#btn23").click(function(){
        confirm("Are you sure you want to delete this record?!");
        $(".grid2").remove();
           });
        });
$(document).ready(function(){          
        $("#btn24").click(function(){
        confirm("Are you sure you want to delete this record?!");
        $(".grid3").remove();
               });
        });
 
$(document).ready(function(){
        $("#btn25").click(function(){
        confirm("Are you sure you want to delete this record?!");
        $(".grid4").remove();
               });
        });

//$(document).ready(function(){
//        $("#delete").click(function(){
//        confirm("Are you sure you want to delete this record?!");
//        window.location.href = '../UI/html/list.html';
//               });
//        });

var deleteLinks = document.querySelectorAll('.delete');

for (var i = 0; i < deleteLinks.length; i++) {
  deleteLinks[i].addEventListener('click', function(event) {
      event.preventDefault();

      var choice = confirm("Are you sure you want to delete this record?!");

      if (choice) {
        window.location.href = 'list.html';
      }
  });
}