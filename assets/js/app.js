// to render products on the index.html, fetch from the endpoint
async function fetchProducts(query = null) {
  try {
    const response = query
      ? await axios.post("http://localhost:8000/products/search", { query })
      : await axios.get("http://127.0.0.1:8000/product/all");
    renderProducts(response.data);
  } catch (error) {
    console.error("Error fetching products:", error);
  }
}

// Function to render products
function renderProducts(products) {
  const productContainer = document.getElementById("product-container");
  productContainer.innerHTML = products
    .map(
      (product) => `
      <div class="col">
        <div class="card h-100">
          <img src="${product.image}" class="card-img-top" alt="${product.name}">
          <div class="card-body">
            <h5 class="card-title">${product.name}</h5>
            <h6 class="card-subtitle mb-2 text-body-secondary">$ ${product.price}</h6>
            <p class="card-text">${product.description}</p>
            <a href="#" class="card-link"><span class="material-symbols-outlined">add_shopping_cart</span></a>
            <a href="#" class="card-link">
              <button type="button" class="btn btn-primary">Buy</button>
            </a>
          </div>
        </div>
      </div>
    `
    )
    .join("");
}

// to render product detail on the detail.html, fetch from the endpoint
async function fetchProductDetails(id) {
  try {
    const response = await axios.get(`http://localhost:8000/product/${id}`);
    renderProductDetails(response.data);
  } catch (error) {
    console.error("Error fetching product details:", error);
  }
}

// render result from result
function renderProductDetails(product) {
  document.getElementById("product-image").src = product.image;
  document.getElementById("product-title").textContent = product.name;
  document.getElementById("product-price").textContent = `$${product.price}`;
  document.getElementById("product-description").textContent =
    product.description;
  document.getElementById("buy-button").onclick = () => addToCart(product.id);
}

// Function to add product to cart
function addToCart(productId) {
  console.log(`Product ${productId} added to cart`);
}

document.addEventListener("DOMContentLoaded", () => {
  const urlParams = new URLSearchParams(window.location.search);
  const productId = urlParams.get("id");
  const query = urlParams.get("query");

  if (productId) {
    fetchProductDetails(productId);
  } else if (query) {
    fetchProducts(query);
  } else {
    fetchProducts();
  }
});
