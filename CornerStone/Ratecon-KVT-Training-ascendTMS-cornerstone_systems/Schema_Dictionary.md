# Rate confirmation Schema Dictionary

<h2> Rate Confirmation Base Schema </h2>

- Rate Confirmation main DICTIONARY

```python
rate_confirmation_schema = {
                            "transaction_type": "204",   
                            "sender": None,  # BROKER or SHIPPER if they are not having a broker. Example: "Werner Logistics"
                            "receiver": {
                                          "name": None,  # carrier-name on top right of page
                                          "isa_qual": "ZZ",  ### hard-coded
                                          "isa_ID": None # client email
                                        }, 
                            "client": None,  ### hard-coded. Example: "Werner Logistics"
                            "submitted_time": None,  # time we received the email
                            "identifier": None, 
                            "identifier_type": None, 
                            "shipment": {
                                          "equipment_number": None, 
                                          "weight": None, 
                                          "weight_unit_code": None, 
                                          "weight_qualifier": "GROSS WEIGHT",  ### hard-coded
                                          "volume": None, 
                                          "volume_qualifier": None, 
                                          "truck_type": None, 
                                          "temperature": None, 
                                          "trucklength": None, 
                                          "charges": None, 
                                          "loading_quantity": None
                                        }, 
                            "purpose": "ORIGINAL",
                            "references": [],  # append references_schema here for reference numbers ABOVE Shipper/Consignee
                            "dates": [],  # append dates_schema here if any, don't include stop dates
                            "notes": [],  # append notes_schema here for notes/comments ABOVE Shipper/Consignee
                            "entities": [],  # append entities_schema here
                            "stops": [],  # append stops_schema here
                            }
```

<h2> Stop Schema </h2>
- entity DICTIONARY to be appended to "stops" in main DICTIONARY.
- It is of two types  
  - PICK (LD),
  - DROP (UL)
- Each stops has it's own "entities", "references" and "notes".

```python
stop_schema = { 
                "stoptype": None,  # see stoptype codes for pickups and drops 
                "_stoptype": None,  # see stoptype codes for pickups and drops
                "ordinal": 1,  # starts from 1 EX: 1,2,3
                "dates": [],  # append dates_schema here
                "references": [],  # append references_schema here for stop references
                "order_detail": [
                                    { 
                                    "purchase_order_number": [],  # append purchase_order_schema here if multiple PO's or single PO
                                    }
                                        ],
                "entities": [],  # append entities_schema here for stop-level entities
                "notes": []  # append notes_schema here for stop-level notes/comments                  
        }
```

<h2> Entities Schema </h2>

- entity DICTIONARY to be appended to "entities" in main DICTIONARY.
- Or, gets appended to individual stops of "stops" DICTIONARY.
- It is of three types  
  - SHIPPER,
  - CONSIGNEE,
  - BROKER

```python

entity_schema = { 
                    "name": None, 
                    "type": None, 
                    "_type": None, 
                    "id": "10",  # hard-coded 
                    "idtype": "MUTUALLY DEFINED",  ## hard-coded 
                    "_idtype": "ZZ",  ## hard-coded 
                    "address": [], # List object ['address part 1', 'address part 2']
                    "city": None, 
                    "state": None, 
                    "postal": None, 
                    "country": None, 
                    "contacts": { 
                                    "contactname": None, 
                                    "contact_type": None, 
                                    "contact_number": None, 
                                    "contact_number_type": None
                                }
                }
```

<h2> Notes Schema </h2>
- note DICTIONARY to be appended to "notes" in main DICTIONARY.
- Or, gets appended to individual stops of "stops" DICTIONARY.

```python
note_schema = {
                "note": None, 
                "notetype": None, 
                "_notetype": None
            }
```

<h2> References Schema </h2>

- This contains bill number, and other references that is there in the rate confirmations.
- references DICTIONARY to be appended to "references" in main DICTIONARY.
- Or, gets appended to individual stops of "stops" DICTIONARY.
[REFERENCE IDENTIFICATION QUALIFIER](https://ediacademy.com/blog/x12-reference-identification-qualifier/)
```python

reference_schema = {
                        "id": None,
                        "idtype": None,
                        "_idtype": None
                    }

```

<h2> Purchase Order Schema </h2>

- purchase_order DICTIONARY to be appended to "order_detail" in stops dictionary IF:
  - if only ONE PO, fill out "stops"["order_detail"] and ignore this extra dictionary.
  - if multiple PO's use this dictionary and append to "order_detail"["purchase_order_number"] in stops dictionary.

```python
purchase_order_schema = {
                        "purchase_order_number": None,
                        "date": None,
                        "cases": None,  # quantity
                        "weight_unit_code": None,  # "L" for pounds, "K" for Kilo
                        "weight": None,
                        "volume_type": None,  # "cubic feet", etc
                        "volume_units": None
                    }
```


<h2> Date Schema </h2>

- date DICTIONARY to be appended to "dates" in main DICTIONARY.
- Or, gets appended to individual stops of "stops" DICTIONARY.

```python
dates_schema = {
                  "date": None,  # dd/mm/yyyy hh:mm
                  "datetype": None,  # always "RESPOND BY", "EP", or "LP"?None
                  "time": None, 
                  "timetype": None  # always "MUST RESPOND BY", "EARLIEST REQUESTED (PICKUP|DROP) TIME", "LATEST REQUESTED (PICKUP|DROP) TIME"?
                }
```
