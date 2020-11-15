<template>
  <div class="t-footer">
      <div class="logo"><router-link to="/"> <img src="@/assets/logo.png" /></router-link></div>
    <div class="footer">
    <a href="#">Разработка &copy; NotBad</a>
  </div>
  </div>
</template>

<script>
import axios from "axios";

export default {};
</script>

<style>

.t-footer .footer {
  background: #001C23;
  width: 100%;
  height: 55px;
  border-top: 2px solid #fff;
  text-align: center;
}

.t-footer .footer > a {
  font-family: SF UI Text;
  font-size: 18px;
  font-style: normal;
  font-weight: 400;
  line-height: 45px;
  letter-spacing: 0em;
  text-align: left;
  color: #fff;
  margin-left: 26px;
  float: left;
}

.t-footer .logo {
  position: absolute;
  top: 6.5px;
  width: 90%;
  right: 0;
  margin: 0;
  height: 30px;
  float: right;
  margin-right: 26px;
}

.t-footer .logo img {
  margin: 0 auto;
  height: 30px;
  float: right;
}
 .button:hover {
  cursor: pointer;
}
.t-footer{
    position: absolute;
    bottom: 0;
    width: 100%;
}
@media only screen and (max-width: 500px){
.t-footer{
    display: none;
}
}
</style>
