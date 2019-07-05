<!DOCTYPE html>
<html>
 <head>
  <title>IIITD|TechTable</title>
  <script src=https://code.jquery.com/jquery-3.3.1.js></script>
  <script src=https://cdn.datatables.net/responsive/2.2.3/css/responsive.bootstrap.min.css></script>
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
   max-width:600px;
   width:100%;
   margin: 0 auto;;
  }
  /* For padding above and below the header and footer respectively*/
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
    td.details-control {
     background: url('../resources/details_open.png') no-repeat center center;
     cursor: pointer;
    }

    tr.shown td.details-control {
     background: url('../resources/details_close.png') no-repeat center center;
    }
   </style>
 </head>
  <body>
    <div class="header">
         <div class="container">
                <a href="https://iiitd.ac.in/"><img src="IIITDLogo.jpg" alt="Home" align="left"></a>
                <img src = "cdt.png" alt="CourseDirectoryTable" width="250" height="125" align="right">
        </div>
    </div>

  <div class="container">
   <br />
   <h2 align="center">Course Table</h2>
   <br />
   <div style="clear:both"></div>
   </form>
   <div class="table-responsive">
    <table class="table table-striped table-bordered" id="data-table">
     <thead>
      <tr>
       <th></th>
       <th>Course Name</th>
       <th>Course Acronym</th>
       <input type="checkbox" checked id="Course Acronym" data-column="2" class="toggle-vis columns">Course Acronym
       <th>Course Code</th>
       <th>Prerequisites</th>
       <input type="checkbox" checked id="Prerequisites" data-column="4" class="toggle-vis columns">Prerequisites
       <th>Antirequisites</th>
       <input type="checkbox" checked id="Antirequisites" data-column="5" class="toggle-vis columns">Antirequisites
       <th>Semester</th>
       <input type="checkbox" checked id="Semester" data-column="6" class="toggle-vis columns">Semester
      </tr>
     </thead>
    </table>
   </div>

   <div class="footer">
        <div class="container">Copyright &copy; 2019 IIITD</div>        
    </div>
 </body>
</html>
<script>

  function format(d){
    return'<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">'+
    '<tr>'+
    '<td>Preferrable Prerequisites:</td>'+
    '<td>'+d.PreferrablePrerequisites+'</td>'+
    '</tr>'+
    '</table>';
  }

$(document).ready(function(){
  // checks if the CSV file was loaded correctly
  $('#data-table').DataTable({
    "ajax": "sampleCourses.json",
    "responsive": true,
    "paging": false,
    "columns" :  [
      {
        "className": 'details-control',
        "orderable": false,
        "data": null,
        "defaultContent": ''
      },
      { "targets": 0,
        data: "Course Name",
        "render": function (data, type, row, meta) {
        var cname=data.substring(0,data.indexOf("#"));
        var link=data.substring(data.indexOf("#")+1);
        return '<a href="'+link+'">'+cname+'</a>';}
        // Hyperlinking the course name with the drive link
      },
      { title: "Course Acronym", data : "Course Acronym" },
      { title: "Course Code", data : "Course Code" },
      { data : "Prerequisites"},
      { data : "Antirequisites"},
      { data : "Semester"}

     ]
  });

  $('#example tbody').on('click', 'td.details-control',function(){
          var tr = $(this).closest('tr');
          var row = table.row(tr);
          if(row.child.isShown()){
            row.child.hide();
            tr.removeClass('shown');
          }
          else{
            row.child(format(row.data())).show();
            tr.addClass('shown');
          }
  });
  $(document).on('change', '.toggleOptions :checkbox', function() {
    var column = table.column( $(this).attr('data-column') ); // Get the column API object
    column.visible( ! column.visible() );  // Toggle the visibility
 });  
});


</script>