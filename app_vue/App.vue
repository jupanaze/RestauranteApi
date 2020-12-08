 <template>
  <div id="app">
    <div class="header">
      <img src=".\assets\logo_carb.png" alt="">  
      <h1>Asados carbón de leña</h1>
      <nav>
        <button v-on:click="init" v-if="is_auth">Inicio</button>
        <button v-on:click="getBalance" v-if="is_auth">Cliente</button>
        <button v-if="is_auth">Inventario</button>
        <button v-if="is_auth">Ventas</button>
        <button v-if="is_auth">Cerrar Sesión</button>
          </nav>
    </div>

    <div class="main-component">
      <form id="form1" onsubmit="getFormvalue()">
        "Usuario: "<br>
        <input type="text" name="usuario" value><br><br>
         "Contraseña: "<br>
        <input type="text" name="contrasena" value><br><br>
        <input type="submit" value="Enviar">
      </form>
    </div>

    <div class="footer">
      <p>Calle 48 # 27-01. Barrancabermeja, Colombia<br>
      Teléfonos: +57 323 590 9805 - 6220238 - 6021901<br>
      E-mail: carbonlena@hotmail.com
    
      </p>
      
    </div>
  </div>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: function () {
    return {
      is_auth: localStorage.getItem("isAuth") || false,
    };
  },

  methods: {},

  beforeCreate: function () {
    localStorage.setItem("current_username", "camilo24");
    localStorage.setItem("isAuth", true);
  },
};
</script>

<style>
body {
  margin: 0 0 0 0;
  background-color: #242424;
}
.header {
  margin: 0%;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #242424;
  color: #f5a018;
  display: flex;
  justify-content: space-between;
  align-items: center;
  vertical-align: middle;
}
.header img{
  width: 90px;
  height: 75px;
  padding: 8%;
}
.header h1 {
  width: 30%;
  text-align: left;
}
.header nav {
  height: 100%;
  width: 45%;

  display: flex;
  justify-content: space-evenly;
  align-items: center;
  padding: 10px;
  font-size: 20px;
}
.header nav button {
  color: #242424;
  background: #f5a018;
  border: 1px solid #e5e7e9;
  border-radius: 2px;
  padding: 10px, 20px;
  cursor: pointer;
}
.header nav button:hover {
  color: #283747;
  background: #e5e7e9;
  border: 1px solid #e5e7e9;
}
.main-component {
  height: 50%;
  margin: 2%;
  text-align: center;
  background: #242424;
  color: #f5a018;
}
.main-component form{
  height: 50%;
  margin: 10% 20% 10% 20%;
  padding: 50px;
  text-align: center;
  background: #242424;
}
.main-component img {
  width: 100px;
  height: 100px; 
  padding: 70px 5%;
}
.footer {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 8vh;
  min-height: 100px;
  background-color: #242424;
  color: #f5a018;
  border-top: 1px solid #f5a018;
}
.footer h2 {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.footer p{
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
