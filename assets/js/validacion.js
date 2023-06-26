function validateForm(event) {
    event.preventDefault(); // Evitar el envío del formulario por defecto
  
    // Obtener los valores de los campos del formulario
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
  
    // Validar los campos
    if (name === "") {
      alert("Por favor, ingresa tu nombre.");
      return false;
    }
    
    if (email === "") {
      alert("Por favor, ingresa tu email.");
      return false;
    }
    
    if (password === "") {
      alert("Por favor, ingresa tu contraseña.");
      return false;
    }
  
    // Si todos los campos son válidos, puedes enviar el formulario o realizar alguna acción adicional
    alert("¡Formulario enviado!");
  
    // Puedes usar AJAX para enviar los datos a un servidor si lo deseas
  }
  
  // Asignar la función de validación al evento 'submit' del formulario
  var form = document.getElementById("myForm");
  form.addEventListener("submit", validateForm);
  


  