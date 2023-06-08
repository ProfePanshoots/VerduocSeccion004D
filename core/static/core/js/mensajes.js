function deleteProducto(id) {   
    Swal.fire({
        title: 'Confirmar',
        text: 'Está seguro que desea eliminar?',
        icon: 'info',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Eliminar'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire('Eliminado!','Producto Eliminado Correctamente','success').then(function() {
              window.location.href = "/delete/"+id+"/";
          })
        }
      })
}

function mensaje(titulo,texto,icono) {
    Swal.fire({
      title: titulo,
      text: texto,
      icon: icono,
      showCancelButton: false,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'success'
    })
}