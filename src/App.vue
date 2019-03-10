<template>
  <div id="app">
<nav class="navbar has-shadow" role="navigation" aria-label="main navigation">
       <div class="container"> 
        <Slide noOverlay>
      <a id="home" href="/">
        <span>Online Store Prices</span>
      </a>
      <a id="home" href="/cinemas">
        <span>Cinema Prices</span>
      </a>
      <a id="home" href="/travelbybus">
        <span>Bus Booking Prices</span>
      </a>
      <a id="home" href="/about">
        <span>About</span>
      </a>
      <a id="home" href="/contact">
        <span>Contact</span>
      </a>
    </Slide>
      </div>
      <a href="/" class="navbar_logo"><img src="./assets/logo.png" width="194px" alt="theLastPrice.com.ng"></a>
</nav>
<router-view/>
<footer class="footer">
  <div class="container">
    <div class="content has-text-centered">
      <p>
        <strong xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" class="blue-text is-2" rel="dct:type">theLastPrice</strong>.com.ng Compare prices online, Online Stores, Cinema ticket prices, Book the cheapest Buses. "Kwee Onu", "Price it". theLastPrice compares prices across ecommerce sites and presents the prices to you for your convenience. Available Online stores are Jumia, Jiji, Konga, Kara and Slot. <strong class="orange-text">the Online Alaroro</strong>. 
      </p>
      <p>Don't Be satisfied with the price you saw, It could be cheaper 😉</p>
      <div class="columns">
        <div class="column is-quarter"><a class="button" href="/">Online Store Prices</a></div>
        <div class="column is-quarter"><a class="button" href="/cinemas">Cinema Prices</a></div>
        <div class="column is-quarter"><a class="button" href="/travelbybus">Bus Booking Prices</a></div>
      </div>
      <p class="has-text-left">Hint: you can remove search results by swiping or dragging them away from the screen</p>
      <p>
        For your <strong>convenience</strong>
      </p>
    </div>
  </div>
</footer>
</div>
</template>

<script>
  import { Slide } from 'vue-burger-menu'
export default {
  name: 'app',
  data () {
    return {
      
    }
  },
  components: {
        Slide // Register your component
    },
}
</script>

<style>

* {
  font-family: 'Dosis', sans-serif;
}

.blue-text{
  color:#212e57;
}
.orange-text{
  color:#fc4a1a;
}
.jumia-text {
  color:#f68b1e;
}
.jiji-text {
  color:#73b747;
}
.konga-text{
  color:#ed017f;
}
.kara-text {
  color:#ba1600;
}
.slot-text {
  color:#dd2400;
}
.content-padding {

  padding-top:30px;
}

.is-lastprice {
      background-color: #212e57;
    }

.bm-burger-button {
      position: fixed;
      width: 30px;
      height: 30px;
      left: 20px;
      top: 10px;
      cursor: pointer;
    }

    .bm-burger-bars {
      background-color: #212e57;
    }

    .bm-menu {
      background-color: #212e57; /* Black*/
    }

  .navbar_logo {
    width: 150px;
    height: 150px;
    margin-left: -70px;
    top: 0px;
    z-index: 200;
    display: block;
    position: absolute;
    left: 50%;
}

</style>
