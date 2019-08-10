<!DOCTYPE html>
<html>
  <head>
    <title>IIITD|Course Directory Table</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
    <script src="https://cdn.datatables.net/1.10.12/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.12/js/dataTables.bootstrap.min.js"></script>  
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.12/css/dataTables.bootstrap.min.css" />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
  
    <style>
    /* Styling for datatable */
    .box
    {
     max-width:500px;
     width:100%;
     margin: 0 auto;;
    }
    body{        
          padding-top: 0px;
          padding-bottom: 0px;
      }
    .header{
          width: 100%;
          background: #ffffff;
          padding: 10px 10px;
          color: #ffffff;
          top: 0;
      }
    .footer{
          width: 100%;
          background: #808080;
          padding: 10px 10px;
          color: #ffffff;
          bottom: 0;
      }
      .footer a {
        float: right;
        color: #ffffff;
        text-align: center;
        padding: 2px 40px;
        text-decoration: none;
      }
      .navbar {
        background-color: #3FADA8;
        top: 0;
        width: 100%;
      }
      .navbar a {
        float: left;
        color: #ffffff;
        text-align: center;
        padding: 10px 10px;
        text-decoration: none;
        font-size: 16px;
      }
      .scrollToTop {
        margin: 0 30px 20px 0;
        position: fixed;
        bottom: 0;
        right: 0;
        display: none;
      }
    </style>
  </head>
  <body>
    <div class="header">
         <div class="container">
                <a href="https://iiitd.ac.in/"><img src="./Images/IIITDLogo.png" alt="Home" align="left"></a>
                <a href="index(v2).php"><img src = "./Images/cdt.png" alt="CourseDirectoryTable" width="200" height="100" align="right"></a>
        </div>
    </div>
    <div class="navbar">
      <a href="https://iiitd.ac.in/">Home</a>
      <a href="#techtree">TechTree</a>
      <a href="https://iiitd.ac.in/contact">Contact</a>
    </div>
    <div class="container">
     <br />
     <h2 align="center">Course Table</h2>
     <br />
      <div style="clear:both"></div>
      <div class="table-responsive">
    <table class="table table-striped table-bordered" id="data-table">
     <thead>
      <tr>
       <th>Course Name</th>
       <th>Course Acronym</th>
       <th>Course Code</th>
       <th>Prerequisites</th>
       <th>Antirequisites</th>
       <th>Semester</th>
      </tr>
     </thead>
    </table>
   </div>
   <a href="#" class="scrollToTop"><img src = "./Images/scroll2top.png" width="30" height="30"></a>
   <div class="footer">
        <div class="container">
          Copyright &copy; 2019 IIITD <a href="credits.html" align="center">Credits</a>
          </div>
    </div>
 </body>
</html>
<script>

$(document).ready(function(){
  // checks if the CSV file was loaded correctly
    var visible = false;
  //Check to see if the window is top if not then display button
  $(window).scroll(function() {
    var scrollTop = $(this).scrollTop();
    if (!visible && scrollTop > 100) {
      $(".scrollToTop").fadeIn();
      visible = true;
    } else if (visible && scrollTop <= 100) {
      $(".scrollToTop").fadeOut();
      visible = false;
    }
  });
  //Click event to scroll to top
  $(".scrollToTop").click(function() {
    $("html, body").animate({
      scrollTop: 0
    }, 800);
    return false;
  });

  $('#data-table').DataTable({
    "ajax": "Courses.json",
    "paging": false,
    "sScrollX": "100%",
    "columns" :  [
      { "targets": 0,
        data: "Course Name",
        "render": function (data, type, row, meta) {
        var cname=data.substring(0,data.indexOf("#"));
        var link=data.substring(data.indexOf("#")+1);
        return '<a href="'+link+'">'+cname+'</a>';}
        // Hyperlinking the course name with the drive link
      },
      { data : "Course Acronym" },
      { data : "Course Code" },
      { data : "Prerequisites"},
      { data : "Antirequisites"},
      { data : "Semester"}

     ]
  });
});
</script>