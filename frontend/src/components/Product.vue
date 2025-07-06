<template>
  <div class="product-card">
    <div class="image-container">
      <div class="action-buttons">
        <span class="icon" @click="toggleLike">{{ isLiked ? '♥︎' : '♡' }}</span>
        <span class="compare">
          <input type="checkbox" v-model="isCompared" />
          <span>Compare</span>
        </span>
      </div>
      <img 
        :src="productImage" 
        :alt="product.title || 'Product image'" 
        class="product-image"
        @error="handleImageError"
      />
    </div>
    <div class="divider"></div>
    <div class="product-info">
      <div class="product-title">{{ product.title || 'Product Title Not Available' }}</div>
      <div class="rating-row" v-if="product.rating || product.reviews">
        <span class="rating-value">{{ product.rating || 'N/A' }}</span>
        <span class="star">★</span>
        <span class="review-count" v-if="product.reviews">({{ product.reviews }})</span>
      </div>
      <div class="price-row">
        <span class="sale-price">{{ product.sale_price || 'Price not available' }}</span>
        <span class="original-price" v-if="product.price">{{ product.price }}</span>
        <span class="discount-message" v-if="discountAmount > 0">(Save ₹{{ discountAmount }})</span>
        <span class="discount-percentage" v-if="discountPercentage > 0">{{ discountPercentage }}% Off</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Product",
  props: {
    product: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      isLiked: false,
      isCompared: false,
      imageError: false,
    };
  },
  computed: {
    productImage() {
      if (!this.product.image || this.imageError) {
        return 'https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1730199583/Croma%20Assets/Entertainment/Television/Images/307846_0_ywdwl1.png?tr=w-400';
      }
      return this.product.image;
    },
    discountAmount() {
      const price = this.cleanPrice(this.product.price);
      const sale = this.cleanPrice(this.product.sale_price);
      return price && sale ? price - sale : 0;
    },
    discountPercentage() {
      const price = this.cleanPrice(this.product.price);
      const sale = this.cleanPrice(this.product.sale_price);
      return price && sale ? Math.round(((price - sale) / price) * 100) : 0;
    },
  },
  methods: {
    cleanPrice(priceStr) {
      if (!priceStr) return 0;
      return parseInt(priceStr.replace(/[₹,]/g, ""), 10);
    },
    toggleLike() {
      this.isLiked = !this.isLiked;
    },
    handleImageError() {
      this.imageError = true;
      console.log('Image failed to load for product:', this.product.title);
    },
  },
};
</script>

<style scoped>
.product-card {
  border-radius: 20px;
  padding: 0 0 28px 0;
  color: #fff;
  display: flex;
  flex-direction: column;
  gap: 0;
  transition: transform 0.2s, box-shadow 0.2s;
  align-items: center;
  min-width: 320px;
  max-width: 400px;
  margin: 0 auto;
}

.product-card:hover {
  transform: translateY(-8px) scale(1.03);
  box-shadow: 0 12px 40px 0 rgba(0,0,0,0.32);
}

.image-container {
  position: relative;
  background-color: #3a3737;
  padding: 15px 15px 0 15px;
  border-radius: 13px 13px 13px 13px;
  overflow: hidden;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 220px;
}

.product-image {
  width: 100%;
  max-width: 350px;
  height: 250px;
  object-fit: contain;
  border-radius: 12px;
}

.divider {
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, #232323 0%, #444 50%, #232323 100%);
  margin: 18px 0 0 0;
  opacity: 0.5;
}

.product-info {
  width: 100%;
  padding: 0 28px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 22px;
}

.product-title {
  font-size: 19px;
  font-weight: bold;
  margin-bottom: 12px;
  color: #fff;
  text-align: left;
  line-height: 1.3;
}

.rating-row {
  display: flex;
  align-items: center;
  gap: 4px;
  color: #12daa8;
  font-size: 15px;
  margin-bottom: 8px;
}

.rating-value {
  font-weight: bold;
  color: #12daa8;
  font-size: 15px;
}

.star {
  font-size: 15px;
  color: #12daa8;
  margin-left: 1px;
}

.review-count {
  color: #bdbdbd;
  font-size: 14px;
  margin-left: 2px;
}

.price-row {
  display: flex;
  align-items: baseline;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 2px;
}

.sale-price {
  font-size: 24px;
  font-weight: bold;
  color: #fff;
}

.original-price {
  font-size: 16px;
  color: #aaa;
  text-decoration: line-through;
  margin-left: 2px;
}

.discount-message {
  font-size: 14px;
  color: #aaa;
  margin-left: 2px;
}

.discount-percentage {
  font-size: 16px;
  border: 1px solid #393737;
  padding: 3px 16px;
  border-radius: 8px;
  font-weight: bold;
  font-family: 'Gotham', sans-serif;
  text-align: center;
  margin-left: 6px;
  letter-spacing: 0.5px;
}

.action-buttons {
  position: absolute;
  top: 16px;
  right: 16px;
  display: flex;
  gap: 14px;
  align-items: center;
  z-index: 2;
}

.icon {
  font-size: 22px;
  cursor: pointer;
  color: white;
  background-color: #292828;
  border: 1.5px solid rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: color 0.3s;
}

.icon:hover {
  color: #12daa8;
  background-color: #292828;
  border: 1.5px solid rgba(255, 255, 255, 0.5);
}

.compare {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 16px;
  color: white;
  background-color: #292828;
  border: 1.5px solid rgba(255, 255, 255, 0.5); 
  border-radius: 20px;
  padding: 5px 18px;
  font-weight: 600;
  transition: background-color 0.3s, color 0.3s;
}

.compare input[type="checkbox"] {
  accent-color: #12daa8;
  width: 16px;
  height: 16px;
  margin-right: 4px;
  cursor: pointer;
}

.compare input[type="checkbox"]:hover,
.compare input[type="checkbox"]:checked {
  accent-color: #12daa8;
}

.compare:hover {
  background-color: #292828;
  color: white;
  border: 1.5px solid rgba(255, 255, 255, 0.5);
}
</style>
