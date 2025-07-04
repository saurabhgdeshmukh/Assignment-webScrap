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
      <img :src="product.image" alt="Product image" class="product-image" />
    </div>

    <h3 class="product-title">{{ product.title }}</h3>

    <div class="rating">
      <span class="rating-value">{{ product.rating }}</span>
      <span class="star">★</span>
      <span class="review-count">({{ product.reviews }})</span>
    </div>

    <div class="price-section">
      <div class="price-info">
        <div class="sale-price">{{ product.sale_price }}</div>
        <div class="original-price">{{ product.price }}</div>
        <div class="discount-message">
          (Save ₹{{ discountAmount }})
        </div>
      </div>
      <div class="discount-percentage">{{ discountPercentage }}% Off</div>
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
    };
  },
  computed: {
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
  },
};
</script>

<style scoped>
.product-card {
  border-radius: 12px;
  padding: 16px;
  color: #fff;
  display: flex;
  flex-direction: column;
  gap: 8px;
  transition: transform 0.2s;
}

.product-card:hover {
  transform: translateY(-4px);
}

.image-container {
  position: relative;
  background-color: #333;
  padding: 10px;
  border-radius: 8px;
  overflow: hidden;
}

.product-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.action-buttons {
  position: absolute;
  top: 8px;
  right: 8px;
  display: flex;
  gap: 8px;
  align-items: center;
}

.icon {
  font-size: 16px;
  cursor: pointer;
  color: white;
  background-color: #292828;
  border: 0.8px solid rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  width: 32px;
  height: 32px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: background-color 0.3s;
}

.icon:hover {
  background-color: #3a3a3a;
}

.compare {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 13px;
  color: white;
  background-color: #292828;
  border: 0.8px solid rgba(255, 255, 255, 0.5); 
  border-radius: 20px;
  padding: 4px 10px;
  font-weight: 600;
  transition: background-color 0.3s;
}

.compare:hover {
  background-color: #3a3a3a;
}

/* .compare input[type="checkbox"] {
  display: none;
} */


.product-title {
  font-size: 16px;
  font-weight: bold;
}

.rating {
  display: flex;
  align-items: center;
  gap: 4px;
  color: #00e6e6;
  font-size: 14px;
}

.rating-value {
  font-weight: bold;
}

.star {
  font-size: 12px;
}

.review-count {
  color: #aaa;
}

.price-section {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  width: 100%;
}

.price-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.sale-price {
  font-size: 20px;
  font-weight: bold;
}

.original-price {
  font-size: 14px;
  color: #aaa;
  text-decoration: line-through;
}

.discount-message {
  font-size: 12px;
  color: #aaa;
}

.discount-percentage {
  font-size: 12px;
  color: rgb(255, 255, 255);
  background-color: #121212;
  padding: 2px 6px;
  border: thin solid #484444;
  border-radius: 3px;
  font-weight: bold;
  font-family: 'Gotham', sans-serif;
  text-align: center;
}
</style>
