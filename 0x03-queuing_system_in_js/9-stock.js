import { listenerCount } from 'process';
import redis from 'redis';
import {promisify}  from 'util';

const listProducts = [
    {
        id: 1,
        name: "Suitcase 250",
        price: 50,
        stock: 4,
    },
    {
        id: 2,
        name: "Suitcase 450",
        price: 100,
        stock: 10,
    },
    {
        id: 3,
        name: "Suitcase 650",
        price: 350,
        stock: 2,
    },
    {
        id: 4,
        name: "Suitcase 1050",
        price: 550,
        stock: 5,
    }
]


const getItemById = id => {
    const item = listProducts.find((entry) => entry.id === +id);
    return item;
}

const client = redis.createClient();

const reserveStockById = (itemId, stock) => {
    client.set(`item.${itemId}`, stock)
}


const getCurrentReservedStockById = async itemId => {
    const getItem  = await promisify(client.get).bind(client, `item.${itemId}`);
    const item = await getItem();
    return item
}


const express = require('express');
const app = express()
const port = 1245;

app.listen(port);


app.get('/list_products', (req, res) => {
    const products = listProducts.map((item) => ({
        itemId: item.id,
        itemName: item.name,
        price: item.price,
        initialAvailabilityQuantity: item.stock
    }))
    res.json(products);
})


app.get('/list_products/:itemId', (req, res) => {
    const {itemId} = req.params;
    const item = getItemById(itemId);
    if (item == undefined) {
        res.json({
            status: "Product not found"
        })
        return;
    }
    getCurrentReservedStockById(itemId).then(stock => {
        const currentStock = item.stock - (stock ?? 0)
        res.json({
            itemId: item.id,
            itemName: item.name,
            price: item.price,
            initialAvailabilityQuantity: item.stock,
            currentQuantity: currentStock
        });
    });
    
})


app.get('/reserve_product/:itemId', (req, res) => {
    const { itemId } = req.params;
    const item = getItemById(itemId);
    if (item == undefined) {
        res.json({
            status: "Product not found"
        })
        return;
    }
    getCurrentReservedStockById(itemId).then(stock => {
        console.log(stock)
        let currentStock = item.stock - (stock ?? 0);
        if (currentStock <= 0) {
            res.json({
                "status": "Not enough stock available",
                "itemId": itemId
            })
        } else {
            reserveStockById(itemId, (+stock) + 1);
            res.json({
                "status": "Reservation confirmed",
                "itemId": itemId
            });
        }
        
    })

})