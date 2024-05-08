// Import required modules
const express = require('express');
const { promisify } = require('util');
const redis = require('redis');
const kue = require('kue');

// Create Redis client
const client = redis.createClient();

// Promisify Redis functions
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Create Express app
const app = express();
const port = 1245;

// Data
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

// Data access
const getItemById = (id) => {
  return listProducts.find(product => product.itemId === id);
};

// Server routes
app.get('/list_products', (req, res) => {
  res.json(listProducts.map(product => ({
    itemId: product.itemId,
    itemName: product.itemName,
    price: product.price,
    initialAvailableQuantity: product.initialAvailableQuantity
  })));
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (product) {
    const reservedStock = await getCurrentReservedStockById(itemId);
    const currentQuantity = product.initialAvailableQuantity - reservedStock;
    res.json({
      itemId: product.itemId,
      itemName: product.itemName,
      price: product.price,
      initialAvailableQuantity: product.initialAvailableQuantity,
      currentQuantity: currentQuantity
    });
  } else {
    res.json({ status: 'Product not found' });
  }
});

// Redis integration
const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const reservedStock = await getAsync(`item.${itemId}`);
  return parseInt(reservedStock) || 0;
};

// Reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }
  const reservedStock = await getCurrentReservedStockById(itemId);
  if (reservedStock >= product.initialAvailableQuantity) {
    res.json({ status: 'Not enough stock available', itemId: itemId });
  } else {
    await reserveStockById(itemId, reservedStock + 1);
    res.json({ status: 'Reservation confirmed', itemId: itemId });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

// Handle errors
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something went wrong!');
});

// Create Kue queue
const queue = kue.createQueue();

// Export app for testing purposes
module.exports = app;

