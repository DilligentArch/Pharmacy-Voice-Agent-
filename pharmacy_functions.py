# Simple in-memory storage
ORDERS_DB = {"orders": {}, "next_id": 1}
DRUG_DB = {

    "napa": {"name": "Napa (Paracetamol)", "price": 2.00,
             "description": "Most popular medicine in Bangladesh for fever, headache, and body pain",
             "quantity": 50},

    "aspirin": {"name": "Ascard (Aspirin)", "price": 3.50,
                "description": "Low-dose aspirin used as blood thinner and for cardiac protection",
                "quantity": 30},

    "ibuprofen": {"name": "Fenbid (Ibuprofen)", "price": 5.00,
                  "description": "Pain reliever and anti-inflammatory for arthritis, muscle pain, and fever",
                  "quantity": 20},


    "metformin": {"name": "Glucomet (Metformin Hydrochloride)", "price": 8.00,
                  "description": "First-line antidiabetic medicine for type 2 diabetes",
                  "quantity": 60},


    "amlodipine": {"name": "Amdocal (Amlodipine Besylate)", "price": 7.00,
                   "description": "Calcium channel blocker for high blood pressure and angina",
                   "quantity": 30},

    "lisinopril": {"name": "Zestril (Lisinopril)", "price": 6.50,
                   "description": "ACE inhibitor for hypertension and heart failure",
                   "quantity": 30},

    "metoprolol": {"name": "Betaloc (Metoprolol Tartrate)", "price": 6.00,
                   "description": "Beta-blocker for hypertension, arrhythmia, and heart protection",
                   "quantity": 30},


    "atorvastatin": {"name": "Ator (Atorvastatin Calcium)", "price": 12.00,
                     "description": "Statin for cholesterol control and cardiovascular protection",
                     "quantity": 30},


    "omeprazole": {"name": "Losec (Omeprazole)", "price": 9.00,
                   "description": "Proton pump inhibitor for ulcer, acid reflux, and gastritis",
                   "quantity": 28},

    "antacid": {"name": "Antacid Plus (Magnesium Hydroxide + Aluminium Hydroxide)", "price": 4.00,
                "description": "Used for quick relief from acidity, indigestion, and heartburn",
                "quantity": 20},


    "ciprofloxacin": {"name": "Ciprocin (Ciprofloxacin)", "price": 14.00,
                      "description": "Broad-spectrum antibiotic for bacterial infections, diarrhea, and UTI",
                      "quantity": 20},

    "azithromycin": {"name": "Zimax / Azee (Azithromycin)", "price": 18.00,
                     "description": "Popular antibiotic for respiratory tract infections, typhoid, and fever",
                     "quantity": 10},


    "cetirizine": {"name": "Histacin (Cetirizine)", "price": 3.00,
                   "description": "Antihistamine for allergy, sneezing, runny nose, and cold symptoms",
                   "quantity": 25},

    "loratadine": {"name": "Clarityne (Loratadine)", "price": 5.00,
                   "description": "Non-drowsy antihistamine for allergy and seasonal flu symptoms",
                   "quantity": 20},


    "sertraline": {"name": "Serlift (Sertraline Hydrochloride)", "price": 11.00,
                   "description": "SSRI antidepressant for depression, anxiety, and panic disorder",
                   "quantity": 30}
}



def get_drug_info(drug_name):
    """Get drug information."""
    drug = DRUG_DB.get(drug_name.lower())
    if drug:
        return {
            "name": drug["name"],
            "description": drug["description"],
            "price": drug["price"],
            "quantity": drug["quantity"]
        }
    return {"error": f"Drug '{drug_name}' not found"}


def place_order(customer_name, drug_name):
    """Place a simple order with predefined quantity."""
    drug = DRUG_DB.get(drug_name.lower())
    if not drug:
        return {"error": f"Drug '{drug_name}' not found"}

    order_id = ORDERS_DB["next_id"]
    ORDERS_DB["next_id"] += 1

    order = {
        "id": order_id,
        "customer": customer_name,
        "drug": drug["name"],
        "quantity": drug["quantity"],
        "total": drug["price"],
        "status": "pending"
    }
    ORDERS_DB["orders"][order_id] = order

    return {
        "order_id": order_id,
        "message": f"Order {order_id} placed: {drug['quantity']} {drug['name']} for ${order['total']:.2f}",
        "total": order['total'],
        "quantity": drug['quantity']
    }


def lookup_order(order_id):
    """Look up an order."""
    order = ORDERS_DB["orders"].get(int(order_id))
    if order:
        return {
            "order_id": order_id,
            "customer": order["customer"],
            "drug": order["drug"],
            "quantity": order["quantity"],
            "total": order["total"],
            "status": order["status"]
        }
    return {"error": f"Order {order_id} not found"}


# Function mapping dictionary
FUNCTION_MAP = {
    'get_drug_info': get_drug_info,
    'place_order': place_order,
    'lookup_order': lookup_order
}