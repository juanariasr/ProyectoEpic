$(document).ready(function(){
    $('#btnSend').click(function(){
        var errores = ''

        // Validando el nombre 
        if( $('#names').val() == ''){
            errores += '<p>Escriba su nombre<p>'
            $('#names').css("border-bottom-color", "#F14B4B")
        } else{
            $('#names').css("border-bottom-color", "#d1d1d1")

        }
        // Validando el correo
        if( $('#email').val() == ''){
            errores += '<p>Escriba su correo<p>'
            $('#email').css("border-bottom-color", "#F14B4B")
        }else{
            $('#email').css("border-bottom-color", "#d1d1d1")

        }
        // Validando el mensaje
        if( $('#mensaje').val() == ''){
            errores += '<p>Escriba un mensaje<p>'
            $('#mensaje').css("border-bottom-color", "#F14B4B")
        }else{
            $('#mensaje').css("border-bottom-color", "#d1d1d1")

        }

        //Enviando el mensaje de los errores
        if( errores == '' == false){
            var mensajeModal = '<div class="modal_wrap">'+
                                    '<div class="mensaje_modal">'+
                                        '<h3>Error</h3>'+
                                        errores+
                                        '<span id="btnClose">Cerrar</span>'+
                                    '</div>'+
                                '</div>'
            $('body').append(mensajeModal) 

            // Cerrando Modal
            $('#btnClose').click(function(){
                $('.modal_wrap').remove()
            })

        }
    })
})