async function fetchProducts(filters = {}) {
    let url = '/products?';
    if (filters.category) url += `category=${filters.category}&`;
    if (filters.max_price) url += `max_price=${filters.max_price}`;
    // Name based filter
    if (filters.q) url += `q=${filters.q}`; 

    const res = await fetch(url);
    const data = await res.json();
    renderProducts(data);
}

function renderProducts(products) {
    const gallery = document.getElementById('gallery');
    gallery.innerHTML = '';

    if (products.length === 0) {
        gallery.innerHTML = '<p>No products found.</p>';
        return;
    }

    products.forEach(p => {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <img src="${p.image}" alt="${p.name}">
            <h3>${p.name}</h3>
            <p>₹${p.price}</p>
            <span>${p.category}</span>
        `;
        gallery.appendChild(card);
    });
}

function applyFilters() {
    const category = document.getElementById('categoryFilter').value;
    const max_price = document.getElementById('priceFilter').value;
    const q = document.getElementById('searchInput').value;
    fetchProducts({ category, max_price, q });
}

// 🔍 Live search functionality
document.getElementById('searchInput').addEventListener('input', () => {
    applyFilters();
});


window.onload = () => fetchProducts();


