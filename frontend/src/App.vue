<template>
  <div class="app">
    <Navbar />
    <div class="section-header">
      <div class="subtitle">Televisions & Accessories</div>
      <div class="title">Televisions & Accessories <span class="count">({{ products.length }})</span></div>
    </div>
    <div class="product-grid-wrapper">
      <div class="product-grid">
        <Product
          v-for="product in products"
          :key="product.title"
          :product="product"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Product from "@/components/Product.vue";
import Navbar from "@/components/Navbar.vue";

export default {
  name: "Home",
  components: {
    Navbar,
    Product,
  },
  data() {
    return {
      products: [],
    };
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      try {
        // Use proxy configuration to avoid CORS issues
        const response = await axios.get("/api/scraped-products");
        if (response.data.success) {
          this.products = response.data.data;
        } else {
          console.error("No products found:", response.data.message);
        }
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    },
  },
};
</script>


<style scoped>
.app {
  font-family: 'Gotham', sans-serif;
  background-color: #181818;
  color: #fff;
  min-height: 100vh;
  margin: 0;
  padding: 0;
  width: 100vw;
  box-sizing: border-box;
}

.section-header {
  margin: 0;
  padding: 40px 0 0 0;
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
}
.subtitle {
  font-size: 18px;
  color: #bdbdbd;
  font-weight: 500;
  margin-bottom: 0.2em;
  margin-left: 8px;
}
.title {
  font-size: 2.5rem;
  font-weight: bold;
  color: #fff;
  margin-bottom: 0.5em;
  margin-left: 8px;
}
.count {
  color: #bdbdbd;
  font-size: 1.2rem;
  font-weight: 400;
}

.product-grid-wrapper {
  width: 100vw;
  display: flex;
  justify-content: center;
  margin: 0;
  padding: 0;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 40px;
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 40px 0 0 0;
}

@media (max-width: 900px) {
  .product-grid {
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 24px;
    padding: 24px 0 0 0;
  }
  .section-header {
    padding: 24px 0 0 0;
  }
}

/* Global styles to remove default margins and padding */
:global(*) {
  box-sizing: border-box;
}

:global(body) {
  margin: 0;
  padding: 0;
  font-family: 'Gotham', sans-serif;
}

:global(html) {
  margin: 0;
  padding: 0;
}
</style>
