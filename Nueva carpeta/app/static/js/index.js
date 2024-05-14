const listProductos= async()=>{
    try{
        const reponse= await fetch('http://127.0.0.1:8000/app/list_productos/')
        const data= await reponse.json();
        let content = '';
        data.Producto.forEach((Productos, index) => {
            content+=`
                <tr>
                    <td>${index+1}</td>
                    <td>${Productos.Nombre}</td>
                    <td>${Productos.Presentacion}</td>
                    <td>${Productos.Cantidad}</td>
                </tr>
            `;
        });
        tabla_cuerpo.innerHTML=content;
    }catch(ex){
        alert(ex)
    }
};

 


window.addEventListener('load', async() =>{
    await listProductos();
});

