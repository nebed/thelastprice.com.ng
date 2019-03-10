<template>
	<vue-slider :value="value" v-on:input="$emit('input', $event)" v-bind="options">
  </vue-slider> 
</template>

<script>
	import vueSlider from 'vue-slider-component';
	export default {
		components : {vueSlider},
		props: {
    		iniValue: Array,
    		value: { type: [Array, Number, String] }
  		},
		data() {
			return {
				options: {
        eventType: 'auto',
        width: 'auto',
        height: 8,
        dotSize: 20,
        min: this.iniValue[0],
        max: this.iniValue[1],
        interval: 1,
        show: true,
        speed: 0.5,
        disabled: false,
        piecewise: false,
        piecewiseStyle: false,
        piecewiseLabel: false,
        tooltip: "always", // why was this false, you want a tooltip, don't you? Yes i want, but didn't dig in plug setting such a dip untill now.
        tooltipDir: ['bottom','bottom'],
        reverse: false,
        data: null,
        clickable: true,
        realTime: false,
        lazy: false,
        formatter: null,
        bgStyle:  {
  "backgroundColor": "#fff",
  "boxShadow": "inset 0.5px 0.5px 3px 1px rgba(0,0,0,.36)"
},
        sliderStyle: [
  {
    "backgroundColor": "#f7b733"
  },
  {
    "backgroundColor": "#4abdac"
  }
],
        processStyle: {
  "backgroundImage": "-webkit-linear-gradient(left, #f7b733, #4abdac)"
},
        piecewiseActiveStyle: null,
        piecewiseStyle: null,
        tooltipStyle: [
  {
    "backgroundColor": "#f7b733",
    "borderColor": "#f7b733"
  },
  {
    "backgroundColor": "#4abdac",
    "borderColor": "#4abdac"
  }
],
        labelStyle: null,
        labelActiveStyle: null
      },

			}
		},
		watch: {
      value: function (){
         
      }
  }
	}	
</script>

<style>
	
</style>

