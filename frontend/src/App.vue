<template>
  <div class="app">
  <div class="header">
   <Navbar />
  </div>
  <div class="container">
    <h5>Televisions & Accessories</h5>
    <h2>Televisions & Accessories</h2>
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
      products: [
        
      ],
    };
  },

  mounted() {
    // Mock the fetch for now
   this.products = [
  {
    product_id: "1",
    title: "Croma 109 cm (43 inch) Full HD LED Smart Linux TV with Bezel Less Display",
    price: "₹15,990",
    sale_price: "₹18,000",
    discount_message: "Save ₹2,010",
    rating: "3.5",
    reviews: 96,
    stock: "In Stock",
    category: "Television",
    description: "A smart TV with bezel-less design and HD display.",
    image: "https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1729510439/Croma%20Assets/Entertainment/Television/Images/301734_0_vu5bzj.png?tr=w-360",
    link: "https://www.croma.com/product1"
  },
  {
    product_id: "2",
    title: "Croma 139.7 cm (55 inch) 4K Ultra HD LED Google TV with Google Voice Assistant",
    price: "₹30,990",
    sale_price: "₹18,000",
    discount_message: "Save ₹12,990",
    rating: "4.2",
    reviews: 152,
    stock: "Limited Stock",
    category: "Television",
    description: "A 4K UHD TV with voice control and immersive display.",
    image: "https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1729510459/Croma%20Assets/Entertainment/Television/Images/273733_0_w8e4qb.png?tr=w-360",
    link: "https://www.croma.com/product2"
  },
  {
    product_id: "1",
    title: "Croma 109 cm (43 inch) Full HD LED Smart Linux TV with Bezel Less Display",
    price: "₹15,990",
    sale_price: "₹18,000",
    discount_message: "Save ₹2,010",
    rating: "3.5",
    reviews: 96,
    stock: "In Stock",
    category: "Television",
    description: "A smart TV with bezel-less design and HD display.",
    image: "https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1729510439/Croma%20Assets/Entertainment/Television/Images/301734_0_vu5bzj.png?tr=w-360",
    link: "https://www.croma.com/product1"
  },
  {
    product_id: "2",
    title: "Croma 139.7 cm (55 inch) 4K Ultra HD LED Google TV with Google Voice Assistant",
    price: "₹30,990",
    sale_price: "₹18,000",
    discount_message: "Save ₹12,990",
    rating: "4.2",
    reviews: 152,
    stock: "Limited Stock",
    category: "Television",
    description: "A 4K UHD TV with voice control and immersive display.",
    image: "https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1729510459/Croma%20Assets/Entertainment/Television/Images/273733_0_w8e4qb.png?tr=w-360",
    link: "https://www.croma.com/product2"
  },
  {
    product_id: "1",
    title: "Croma 109 cm (43 inch) Full HD LED Smart Linux TV with Bezel Less Display",
    price: "₹15,990",
    sale_price: "₹18,000",
    discount_message: "Save ₹2,010",
    rating: "3.5",
    reviews: 96,
    stock: "In Stock",
    category: "Television",
    description: "A smart TV with bezel-less design and HD display.",
    image: "https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1729510439/Croma%20Assets/Entertainment/Television/Images/301734_0_vu5bzj.png?tr=w-360",
    link: "https://www.croma.com/product1"
  },
  {
    product_id: "2",
    title: "Croma 139.7 cm (55 inch) 4K Ultra HD LED Google TV with Google Voice Assistant",
    price: "₹30,990",
    sale_price: "₹18,000",
    discount_message: "Save ₹12,990",
    rating: "4.2",
    reviews: 152,
    stock: "Limited Stock",
    category: "Television",
    description: "A 4K UHD TV with voice control and immersive display.",
    image: "https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1729510459/Croma%20Assets/Entertainment/Television/Images/273733_0_w8e4qb.png?tr=w-360",
    link: "https://www.croma.com/product2"
  },
  {
    product_id: "1",
    title: "Croma 109 cm (43 inch) Full HD LED Smart Linux TV with Bezel Less Display",
    price: "₹15,990",
    sale_price: "₹18,000",
    discount_message: "Save ₹2,010",
    rating: "3.5",
    reviews: 96,
    stock: "In Stock",
    category: "Television",
    description: "A smart TV with bezel-less design and HD display.",
    image: "https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1729510439/Croma%20Assets/Entertainment/Television/Images/301734_0_vu5bzj.png?tr=w-360",
    link: "https://www.croma.com/product1"
  },
  {
    product_id: "2",
    title: "Croma 139.7 cm (55 inch) 4K Ultra HD LED Google TV with Google Voice Assistant",
    price: "₹30,990",
    sale_price: "₹18,000",
    discount_message: "Save ₹12,990",
    rating: "4.2",
    reviews: 152,
    stock: "Limited Stock",
    category: "Television",
    description: "A 4K UHD TV with voice control and immersive display.",
    image: "https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1729510459/Croma%20Assets/Entertainment/Television/Images/273733_0_w8e4qb.png?tr=w-360",
    link: "https://www.croma.com/product2"
  },
  {
    product_id: "1",
    title: "Croma 109 cm (43 inch) Full HD LED Smart Linux TV with Bezel Less Display",
    price: "₹15,990",
    sale_price: "₹18,000",
    discount_message: "Save ₹2,010",
    rating: "3.5",
    reviews: 96,
    stock: "In Stock",
    category: "Television",
    description: "A smart TV with bezel-less design and HD display.",
    image: "https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1729510439/Croma%20Assets/Entertainment/Television/Images/301734_0_vu5bzj.png?tr=w-360",
    link: "https://www.croma.com/product1"
  },
  {
    product_id: "2",
    title: "Croma 139.7 cm (55 inch) 4K Ultra HD LED Google TV with Google Voice Assistant",
    price: "₹30,990",
    sale_price: "₹18,000",
    discount_message: "Save ₹12,990",
    rating: "4.2",
    reviews: 152,
    stock: "Limited Stock",
    category: "Television",
    description: "A 4K UHD TV with voice control and immersive display.",
    image: "https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1729510459/Croma%20Assets/Entertainment/Television/Images/273733_0_w8e4qb.png?tr=w-360",
    link: "https://www.croma.com/product2"
  },
  {
    product_id: "1",
    title: "Croma 109 cm (43 inch) Full HD LED Smart Linux TV with Bezel Less Display",
    price: "₹15,990",
    sale_price: "₹18,000",
    discount_message: "Save ₹2,010",
    rating: "3.5",
    reviews: 96,
    stock: "In Stock",
    category: "Television",
    description: "A smart TV with bezel-less design and HD display.",
    image: "https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1729510439/Croma%20Assets/Entertainment/Television/Images/301734_0_vu5bzj.png?tr=w-360",
    link: "https://www.croma.com/product1"
  },
  {
    product_id: "2",
    title: "Croma 139.7 cm (55 inch) 4K Ultra HD LED Google TV with Google Voice Assistant",
    price: "₹30,990",
    sale_price: "₹18,000",
    discount_message: "Save ₹12,990",
    rating: "4.2",
    reviews: 152,
    stock: "Limited Stock",
    category: "Television",
    description: "A 4K UHD TV with voice control and immersive display.",
    image: "https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1729510459/Croma%20Assets/Entertainment/Television/Images/273733_0_w8e4qb.png?tr=w-360",
    link: "https://www.croma.com/product2"
  },
];

  },
};
</script>

<style scoped>
.app {
  font-family: 'Gotham', sans-serif;
  background-color: #121212;
  color: #fff;
  min-height: 100vh;
}

.header {
  background-color: #000;
  padding: 10px;
  text-align: center;
  font-size: 24px;
  font-weight: bold;
}

.header span {
  color: #fff;
}

.container {
  padding: 40px;
  background-color:#121212 
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: 30px;
  margin-top: 20px;
}

@media (min-width: 600px) {
  .product-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 900px) {
  .product-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}


</style>
