<!DOCTYPE html>

<html>
<head>
    <title></title>
</head>
<body>
<?php

if (isset($_POST['submit']))
{
	$file= $_FILES['file'];

	$fileName= $_FILES['file']['name'];
    $fileTmpName= $_FILES['file']['tmp_name'];
    $fileSize= $_FILES['file']['size'];
    $fileError= $_FILES['file']['error'];
    $fileType= $_FILES['file']['type'];

    $fileExt = explode('.', $fileName);
    $fileActualExt = strtolower(end($fileExt));

    $allowed = array('jpg', 'jpeg', 'png', 'csv', 'pdf');
    if (in_array($fileActualExt, $allowed))
    {
        if($fileError===0)
        {
            if ($fileSize < 1000000)
            {
// var=using unique id so that in case two files with same name are uploaded, old one doesnt get replaced!? 
                $fileNameNew = uniqid('', true).".".$fileActualExt;
                $fileDestination = 'uploads/'.$fileNameNew;
                move_uploaded_file($fileTmpName, $fileDestination);
                // header("Location: fileupload.html");
                echo "Upload successful";
            }
            else
            {
                echo "Your file is too big!";
            }
        }
        else
        {
            echo "There was an error uploading your file!";
        }
    }

    else
    {
        echo "You cannot upload files of this type!";
    }
} else {
    ?>
        <form action="upload.php" method="POST" enctype="multipart/form-data" >
        <input type="file" name="file">
        <button type="submit" name="submit">UPLOAD</button>
        </form>
    <?php
}
?>
</body>
</html>