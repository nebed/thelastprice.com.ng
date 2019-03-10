<template>

	<div ref="interactElement" class="column interactcard is-full-mobile is-half-tablet is-one-third-desktop"
		:style="{ transform: transformString }"
		:class="{isAnimating: isInteractAnimating}"
	>
		<div class="card">
		  <div class="card-content">
		    <div class="media">
		      <div class="media-left">
		        <figure class="image is-96x96">
		          <img :src=image :alt=title>
		        </figure>
		      </div>
		      <div class="media-content">
		        <p class="title is-5" :title=title v-text="truncateText"></p>
		        <p class="subtitle is-5">₦ {{price}}</p>
		        <button @click="showProduct" :class=store class="button is-fullwidth is-outlined">Buy from {{ store }}</button>
		      </div>
		    </div>
		  </div>
		</div>
	</div>
	
</template>

<script>
	import interact from "interactjs";
	export default {
		static: {
		    interactYThreshold: 150,
		    interactXThreshold: 100
		  },
		props: ['store','image','url','title','price'],

		mounted() {
		  const element = this.$refs.interactElement;
		  interact(element).draggable({
		  	onstart: () => {
		  		this.isInteractAnimating = false;
		  	},
		    onmove: event => {
		      const x = this.interactPosition.x + event.dx;
		      const y = this.interactPosition.y + event.dy;
		      this.interactSetPosition({ x, y });
		    },
		    onend: () => {
		      const { x, y } = this.interactPosition;
		      const { interactXThreshold, interactYThreshold } = this.$options.static;
		      this.isInteractAnimating = true;
		          
		      if (x > interactXThreshold) this.playCard("DELETE_CARD_X");
		      else if (x < -interactXThreshold) this.playCard("DELETE_CARD_x2");
		      else if (y > interactYThreshold) this.playCard("DELETE_CARD_Y");
		      else this.resetCardPosition();
		    }
		  });
		},
// ...
		beforeDestroy() {
		  //interact(this.$refs.interactElement).unset();
		},

		data() {
		  return {
		    interactPosition: {
		      x: 0,
		      y: 0
		    },
		    isInteractAnimating: true,
		  };
		},

		computed: {

			truncateText() {
				if ( this.title.length > 20 ) {
        			return this.title.substring(0,20) + '...';
      			} else {
        			return this.title;
      			}
			},
			transformString() {
			    if (!this.isInteractAnimating) {
			      const { x, y } = this.interactPosition;
			      return `translate3D(${x}px, ${y}px, 0)`;
			    }
			    return null;
			 }
		},

		methods: {
			showProduct() {
              this.$emit('clicked', {'url':this.url, 'store':this.store});
            },
            
			playCard(interaction) {
		    const {
		      interactOutOfSightXCoordinate,
		      interactOutOfSightYCoordinate,
		    } = this.$options.static;

		    //this.interactUnsetElement();

		    switch (interaction) {
		      case "DELETE_CARD_X":
		        this.interactSetPosition({
		          x: interactOutOfSightXCoordinate,
		        });
		        this.$emit('deleted');
		        break;
		      case "DELETE_CARD_x2":
		        this.interactSetPosition({
		          x: -interactOutOfSightXCoordinate,
		        });
		        this.$emit('deleted');
		        break;
		      case "DELETE_CARD_Y":
		        this.interactSetPosition({
		         y: interactOutOfSightYCoordinate
		        });
		        this.$emit("deleted");
		        break;
		    }

		    //this.hideCard();
		  },

		  hideCard() {
		    setTimeout(() => {
		      this.isShowing = false;
		      this.$emit("hideCard", this.card);
		    }, 300);
		  },
		  
		  interactUnsetElement() {
		    interact(this.$refs.interactElement).unset();
		    this.interactDragged = true;
		  },
    
            interactSetPosition(coordinates) { 
			    const { x = 0, y = 0 } = coordinates;
			    this.interactPosition = {x, y };
			  },
			  
			  resetCardPosition() {
			    this.interactSetPosition({ x: 0, y: 0 });
			  },

            showProduct() {
              this.$emit('clicked', {'url':this.url, 'store':this.store});
            }
    	}

	}
</script>

<style>

.interactcard {
  -ms-touch-action: none;
  touch-action: none;
}

	.button.jumia.is-outlined {
    background-color: transparent;
    border-color: #f68b1e;
    color: #f68b1e;
}

.button.jumia.is-outlined:hover, .button.jumia.is-outlined:focus {
    background-color: #f68b1e;
    border-color: #f68b1e;
    color: #fff;
}

.button.konga.is-outlined {
    background-color: transparent;
    border-color: #ed017f;
    color: #ed017f;
}

.button.konga.is-outlined:hover, .button.konga.is-outlined:focus {
    background-color: #ed017f;
    border-color: #ed017f;
    color: #fff;
}

.button.kara.is-outlined {
    background-color: transparent;
    border-color: #ba1600;
    color: #ba1600;
}

.button.kara.is-outlined:hover, .button.kara.is-outlined:focus {
    background-color: #ba1600;
    border-color: #ba1600;
    color: #fff;
}

.button.slot.is-outlined {
    background-color: transparent;
    border-color: #dd2400;
    color: #dd2400;
}

.button.slot.is-outlined:hover, .button.slot.is-outlined:focus {
    background-color: #dd2400;
    border-color: #dd2400;
    color: #fff;
}

.button.jiji.is-outlined {
    background-color: transparent;
    border-color: #73b747;
    color: #73b747;
}

.button.jiji.is-outlined:hover, .button.jiji.is-outlined:focus {
    background-color: #73b747;
    border-color: #73b747;
    color: #fff;
}

 .date {

    position: absolute;
    top: 20px;
    right: 20px;
    z-index: 1;
    background: #e74c3c;
    width: 55px;
    height: 55px;
    padding: 12.5px 0;
    -webkit-border-radius: 100%;
    -moz-border-radius: 100%;
    border-radius: 100%;
    color: #FFFFFF;
    font-weight: 700;
    text-align: center;
    -webkti-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;

}
	
</style>