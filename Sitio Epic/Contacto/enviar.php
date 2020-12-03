<?php 
//Lamando a los campos 

$nombre = $_POST['nombre'];
$telefono = $_POST['telefono'];
$correo = $_POST['correo'];
$mensaje = $_POST['mensaje'];

// Datos para el correo
$destinatario = "pablo.camposa@sansano.usm.cl";
$asunto = "Contacto desde nuestra web";

$carta = "De: $nombre \n";
$carta .= "Correo: $correo \n";
$carta .= "Telefono: $telefono";
$carta .= "Mensaje: $mensaje";

//Enviando correo

mail($destinatario, $asunto, $carta);

?>





