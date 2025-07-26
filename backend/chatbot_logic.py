import pandas as pd

# Load data (cached on first call)
orders = pd.read_csv('data/orders.csv')
order_items = pd.read_csv('data/order_items.csv')
inventory = pd.read_csv('data/inventory_items.csv')

def get_response(message):
    message = message.lower()

    if "top 5" in message or "most sold" in message:
        top = order_items['product_id'].value_counts().head(5)
        return f"Top 5 most sold product IDs: {top.index.tolist()}"

    elif "status of order" in message:
        try:
            order_id = int(''.join(filter(str.isdigit, message)))
            order = orders[orders['order_id'] == order_id]
            if not order.empty:
                return f"Order {order_id} is currently {order['status'].values[0]}"
            else:
                return "Order not found."
        except:
            return "Invalid order ID format."

    elif "how many" in message and "classic t-shirt" in message:
        t_shirt_stock = inventory[
            (inventory['product_name'].str.lower().str.contains("classic t-shirt")) &
            (inventory['sold_at'].isna())
        ]
        return f"There are {len(t_shirt_stock)} Classic T-Shirts in stock."

    else:
        return "Sorry, I didn’t understand that. Try asking about top products or order status."

