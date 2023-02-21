import re
from functions.get_ratecon_schema import (
    get_rate_confirmation_schema, 
    get_stops_schema,
    get_entity_schema, 
    get_reference_schema, 
    get_note_schema, 
    get_dates_schema, 
    get_purchase_order_schema
)

#function for confirmation
def extract(text_map):

    details = get_rate_confirmation_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]

        # if "sender" in details and details["sender"] is None:
        #     details["sender"] = sender(content)
        if "name" in details["receiver"] and details["receiver"]["name"] is None:
            details["receiver"]["name"] = receiver_name(content)
        if "isa_ID" in details["receiver"] and details["receiver"]["isa_ID"] is None:
            details["receiver"]["isa_ID"] = receiver_email(content)
        # if "client" in details and details["client"] is None:
        #     details["client"] = client(content)
        if "submitted_time" in details and details["submitted_time"] is None:
            details["submitted_time"] = submitted_time(content)
        if "identifier" in details and details["identifier"] is None:
            details["identifier"] = identifier(content)
        if "equipment_number" in details["shipment"] and details["shipment"]["equipment_number"] is None:
            details["shipment"]["equipment_number"] = equipment_number(content)
        if "weight" in details["shipment"] and details["shipment"]["weight"] is None:
            details["shipment"]["weight"] = weight(content)        
        if "truck_type" in details["shipment"] and details["shipment"]["truck_type"] is None:
            details["shipment"]["truck_type"] = truck_type(content)
        if "temperature" in details["shipment"] and details["shipment"]["temperature"] is None:
            details["shipment"]["temperature"] = temperature(content)
        if "charges" in details["shipment"] and details["shipment"]["charges"] is None:
            details["shipment"]["charges"] = charges(content)
        if "loading_quantity" in details["shipment"] and details["shipment"]["loading_quantity"] is None:
            details["shipment"]["loading_quantity"] = loading_quantity(content)


    
    
    return details


#function for references 5
def references_sh(text_map):

    details = get_reference_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "id" in details and details["id"] is None:
            details["id"] = id_sh(content)
        if "idtype" in details and details["idtype"] is None:
            details["idtype"] = "SH"
        if "_idtype" in details and details["_idtype"] is None:
            details["_idtype"] = "shipment#"
        
        
    return details

def references_mc(text_map):

    details = get_reference_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "id" in details and details["id"] is None:
            details["id"] = id_mc(content)
        if "idtype" in details and details["idtype"] is None:
            details["idtype"] = "MC#"
        if "_idtype" in details and details["_idtype"] is None:
            details["_idtype"] = "Motor Carrier#"
        
        
    return details

def references_dot(text_map):

    details = get_reference_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "id" in details and details["id"] is None:
            details["id"] = id_dot(content)
        if "idtype" in details and details["idtype"] is None:
            details["idtype"] = "DOT"
        if "_idtype" in details and details["_idtype"] is None:
            details["_idtype"] = "Department of Transportation#"
        
        
    return details

def references_bol(text_map):

    details = get_reference_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "id" in details and details["id"] is None:
            details["id"] = id_bol(content)
        if "idtype" in details and details["idtype"] is None:
            details["idtype"] = "BL"
        if "_idtype" in details and details["_idtype"] is None:
            details["_idtype"] = "BILL OF LANDING"
        
        
    return details

def references_crpo(text_map):

    details = get_reference_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "id" in details and details["id"] is None:
            details["id"] = id_crpo(content)
        if "idtype" in details and details["idtype"] is None:
            details["idtype"] = "CR/PO"
        if "_idtype" in details and details["_idtype"] is None:
            details["_idtype"] = "Cust Ref/PO#"
        
        
    return details


#function for date pickup
def date_pick(text_map):

    details = get_dates_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "date" in details and details["date"] is None:
            details["date"] = date_pickup(content)
        if "datetype" in details and details["datetype"] is None:
            details["datetype"] = "EP&LP"
        if'timetype' in details and details['timetype'] is None:
            details['timetype'] = "EARLIEST&LATEST PICKUP TIME"

    return details

#function for date dropoff2-7
def date_drop2(text_map):

    details = get_dates_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "date" in details and details["date"] is None:
            details["date"] = date_drop_2(content)
        if "datetype" in details and details["datetype"] is None:
            details["datetype"] = "ED&LD"
        if'timetype' in details and details['timetype'] is None:
            details['timetype'] = "EARLIEST&LATEST delivery TIME"

    return details

def date_drop3(text_map):

    details = get_dates_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "date" in details and details["date"] is None:
            details["date"] = date_drop_3(content)
        if "datetype" in details and details["datetype"] is None:
            details["datetype"] = "ED&LD"
        if'timetype' in details and details['timetype'] is None:
            details['timetype'] = "EARLIEST&LATEST delivery TIME"

    return details

def date_drop4(text_map):

    details = get_dates_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "date" in details and details["date"] is None:
            details["date"] = date_drop_4(content)
        if "datetype" in details and details["datetype"] is None:
            details["datetype"] = "ED&LD"
        if'timetype' in details and details['timetype'] is None:
            details['timetype'] = "EARLIEST&LATEST delivery TIME"

    return details

def date_drop5(text_map):

    details = get_dates_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "date" in details and details["date"] is None:
            details["date"] = date_drop_5(content)
        if "datetype" in details and details["datetype"] is None:
            details["datetype"] = "ED&LD"
        if'timetype' in details and details['timetype'] is None:
            details['timetype'] = "EARLIEST&LATEST delivery TIME"

    return details

def date_drop6(text_map):

    details = get_dates_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "date" in details and details["date"] is None:
            details["date"] = date_drop_6(content)
        if "datetype" in details and details["datetype"] is None:
            details["datetype"] = "ED&LD"
        if'timetype' in details and details['timetype'] is None:
            details['timetype'] = "EARLIEST&LATEST delivery TIME"

    return details

def date_drop7(text_map):

    details = get_dates_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "date" in details and details["date"] is None:
            details["date"] = date_drop_7(content)
        if "datetype" in details and details["datetype"] is None:
            details["datetype"] = "ED&LD"
        if'timetype' in details and details['timetype'] is None:
            details['timetype'] = "EARLIEST&LATEST delivery TIME"

    return details


#function for note
def note(text_map):

    details = get_note_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "note" in details and details["note"] is None:
            details["note"] = shipment_note(content)

    return details

#function for entity shipper
def entities(text_map):

    details = get_entity_schema("SHIPPER")

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "name" in details and details["name"] is None:
            details["name"] = sender(content)
        if "city" in details and details["city"] is None:
            details["city"] = city_shipper(content)
        if "state" in details and details["state"] is None:
            details["state"] = state_shipper(content)
        if "address" in details and details["address"] is None:
            details["address"] = address_shipper(content)
        if "contact_number" in details["contacts"] and details["contacts"]["contact_number" ] is None:
            details["contacts"]["contact_number" ] = pn_shipper(content)
        

    return details

# function for entity delivery
def entities_drop(text_map):

    details = get_entity_schema("CONSIGNEE")

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "city" in details and details["city"] is None:
            details["city"] = city_drop(content)
        if "state" in details and details["state"] is None:
            details["state"] = state_drop(content)
        if "address" in details and details["address"] is None:
            details["address"] = address_drop(content)
        if "contact_number" in details["contacts"] and details["contacts"]["contact_number" ] is None:
            details["contacts"]["contact_number" ] = pn_drop(content)
        

    return details

# function for entity delivery
def entities_broker(text_map):

    details = get_entity_schema("BROKER")

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]

        if "name" in details and details["name"] is None:
            details["name"] = sender(content)
        if "address" in details and details["address"] is None:
            details["address"] = address_broker(content)
        if "contact_number" in details["contacts"] and details["contacts"]["contact_number" ] is None:
            details["contacts"]["contact_number" ] = pn_broker(content)
        if "contactname" in details["contacts"] and details["contacts"]["contactname" ] is None:
            details["contacts"]["contactname" ] = sender(content)
        

    return details

#function for stops pick and drop
def stop_pick(text_map):

    details = get_stops_schema("PICK",1)
        
        
    return details

def stop_drop(text_map):

    details = get_stops_schema("DROP",2)
        
        
    return details


#function for order details
def order_detail(text_map):

    details = get_purchase_order_schema()

    num_pages = len(text_map)

    for page in range(num_pages):
        content = text_map[str(page)]
        if "purchase_order_number" in details and details["purchase_order_number"] is None:
            details["purchase_order_number"] = id_crpo(content)
        if "date" in details and details["date"] is None:
            details["date"] = submitted_time(content)
        if "cases" in details and details["cases"] is None:
            details["cases"] = loading_quantity(content)
        if "weight" in details and details["weight"] is None:
            details["weight"] = weight(content)

    return details
    




# extract sender
def sender(text):
    match = re.search(r'(Sent|backup information By:|Sent;By:|pent|backup) ([\w\s\-]*)', text)
    if match:  
         return match.group(2)
    else:
        return None
# extract reciver name
def receiver_name(text):
    match = re.search(r'Carrier([\w\s\-\d]*)Driver', text)
    if match:  
         return match.group(1)
    else:
        return None
# extract reciver email
def receiver_email(text):
    match = re.search(r'Dispatch Email\s([\w\d\_\$\&\%\-]*@[\w\d\.]*)', text)
    if match:  
         return match.group(1)
    else:
        return None
# extract client
def client(text):
    match = re.search(r'CONSIGNEE:\s([\w\s\d\-]*)APPT', text)
    if match:  
         return match.group(1)
    else:
        return None
# extract submitted_time
def submitted_time(text):
    match = re.search(r'Todays Date\s([\d]*\/[\d]*\/[\d]*\s[\d]*:[\d]*)', text)
    if match:  
         return match.group(1)
    else:
        return None
# extract identifier
def identifier(text):
    match = re.search(r'Shipment\s\#[\s\_\.]*([\d]*)', text)
    if match:  
         return match.group(1)
    else:
        return None
# extract equipment_number
def equipment_number(text):
    match = re.search(r'Eq ID([\w\d]*)', text)
    if match:  
         return match.group(1)
    else:
        return None
# extract weight
def weight(text):
    match = re.search(r'Shipment\s\#[\s\_\.]*([\d]*)', text)
    if match:  
         return match.group(1)
    else:
        return None
# extract truck_type
def truck_type(text):
    match = re.search(r'Eq Type\s([\w\d\'\s]*)', text)
    if match:  
         return match.group(1)
    else:
        return None
# extract temperature
def temperature(text):
    match = re.search(r'Temperature\s([\w\d\-]*)', text)
    if match:  
         return match.group(1)
    else:
        return None
# extract charges
def charges(text):
    match = re.search(r'Total:\s([\w\d\$\,\.]*)', text)
    if match:  
         return match.group(1)
    else:
        return None
# extract loading_quantity
def loading_quantity(text):
    match = re.search(r'(DIMS|Description);([\w\d\s\-\.\;]*)Carrier\sRate', text)#(DIMS|Description);([\w\d\s\-\.\;]*)Carrier\sRate
    if match:
        lst = match.group(2).split()
        if "lbs" in lst:
            if int(lst[0]) == 0:
                PCS=int(lst[0])
                return PCS
            else:
                PCS="".join(lst[:2])
                return PCS
        if "lbs" not in lst:
            if int(lst[0]) == 0 and lst[1].isdigit():
                PCS=lst[0]
                return PCS
        
# extract weight
def weight(text):
    match = re.search(r'(DIMS|Description);([\w\d\s\-\.\;]*)Carrier\sRate', text)#(DIMS|Description);([\w\d\s\-\.\;]*)Carrier\sRate
    if match:
        lst = match.group(2).split()
        if "lbs" in lst:
            for i in lst:
                if i =="lbs":
                    index=lst.index(i)
                    index2=index-1
                    num = lst[index2]
                    weight = num+" "+"lbs"
                    return weight

        if "lbs" not in lst:
            if int(lst[0]) == 0 and lst[1].isdigit():
                weight=lst[2]
                return weight
            else:
                weight=lst[3]
                return weight
    
# extract shipment#
def id_sh(text):
    match = re.search(r'Shipment\s\#[\s\_\.]*([\d]*)', text)
    if match:  
         return match.group(1)
    else:
        return None
# extract bol#
def id_bol(text):
    match = re.search(r'BOL #\s([\w\-\d\s]*)Carrier\sMiles', text)
    if match:  
         return match.group(1)
    else:
        return None
# extract mc#
def id_mc(text):
    match = re.search(r'MC\s([\d]*)', text)
    if match:  
         return match.group(1)
    else:
        return None
# extract shipment#
def id_dot(text):
    match = re.search(r'DOT #\s([\d]*)', text)
    if match:  
         return match.group(1)
    else:
        return None

# extract crpo#
def id_crpo(text):
    match = re.search(r'Cust\sRef\/PO\s\#\s([\w\d\-\s\/\,]*)Eq', text)
    if match:  
         return match.group(1)
    else:
        return None

# extract date pickup#
def date_pickup(text):
    match = re.search(r'Pickup([\s\w\d\,\;]*)Scheduled\s(([\d]*\/[\d]*\/[\d]*)\s[\d]*:[\d]*(;|\s-\s[\d]*:[\d]*|\s))', text)
    if match:  
         return match.group(2)
    else:
        return None
# extract date dropoff2#
def date_drop_2(text):
    match = re.search(r'2 Delivery([\s\w\d\,\;]*)Scheduled\s(([\d]*\/[\d]*\/[\d]*)\s[\d]*:[\d]*(;|\s-\s[\d]*:[\d]*|\s))', text)
    if match:  
         return match.group(2)
    else:
        return None
# extract date dropoff3#
def date_drop_3(text):
    match = re.search(r'3 Delivery([\s\w\d\,\;]*)Scheduled\s(([\d]*\/[\d]*\/[\d]*)\s[\d]*:[\d]*(;|\s-\s[\d]*:[\d]*|\s))', text)
    if match:  
         return match.group(2)
    else:
        return None
# extract date dropoff4#
def date_drop_4(text):
    match = re.search(r'4 Delivery([\s\w\d\,\;]*)Scheduled\s(([\d]*\/[\d]*\/[\d]*)\s[\d]*:[\d]*(;|\s-\s[\d]*:[\d]*|\s))', text)
    if match:  
         return match.group(2)
    else:
        return None
# extract date dropoff5#
def date_drop_5(text):
    match = re.search(r'5 Delivery([\s\w\d\,\;]*)Scheduled\s(([\d]*\/[\d]*\/[\d]*)\s[\d]*:[\d]*(;|\s-\s[\d]*:[\d]*|\s))', text)
    if match:  
         return match.group(2)
    else:
        return None
# extract date dropoff6#
def date_drop_6(text):
    match = re.search(r'6 Delivery([\s\w\d\,\;]*)Scheduled\s(([\d]*\/[\d]*\/[\d]*)\s[\d]*:[\d]*(;|\s-\s[\d]*:[\d]*|\s))', text)
    if match:  
         return match.group(2)
    else:
        return None
# extract date dropoff7#
def date_drop_7(text):
    match = re.search(r'7 Delivery([\s\w\d\,\;]*)Scheduled\s(([\d]*\/[\d]*\/[\d]*)\s[\d]*:[\d]*(;|\s-\s[\d]*:[\d]*|\s))', text)
    if match:  
         return match.group(2)
    else:
        return None

# extract shipment note
def shipment_note(text):
    match = re.search(r'(Shipment|shipment)\s*Notes(\s|;)([\:\s\~\w\d\.\;\/\-\,\!\(\)\<\\\‘]*);([\w\s]*)(EXPRESS|LOGISTICS|LLC|INC);', text)
    if match:  
         return match.group(3)
    else:
        return None

# extract city shipper#
def city_shipper(text):
    match = re.search(r'Pickup\s([\w\d\s]*)Scheduled[\s\d\/\:\-]*;([\w\d\s]*;|)(\w*),\s(\w*),\s(\d*)', text)
    if match: 
        return match.group(3)
    else:
        
        match = re.search(r'Pickup\s(([\w\d\s]*)Scheduled([\s\d\/\:\-]*);([\w\d\s]*;|)|)(\w*),\s(\w*),\s(\d*)',text)
        if match:
            return match.group(5)
        else:
            match = re.search(r'Pickup\s([\w\s]*), (\w*)(,|.) (\d*)',text)
            if match:
                return match.group(1)
            else:
                match = re.search(r'Pickup\sScheduled\s([\s\d\/\:\-]*);([\w\s]*),\s(\w*),\s(\d*)',text)
                if match:
                    return match.group(2)
                else:
                    match = re.search(r'Pickup\s([\d\w\s\,]*);([\w\s]*),\s(\d*)',text)
                    if match:
                        return match.group(2)

# extract state shipper#
def state_shipper(text):
    match = re.search(r'Pickup\s([\w\d\s]*)Scheduled[\s\d\/\:\-]*;([\w\d\s]*;|)(\w*),\s(\w*),\s(\d*)', text)
    if match: 
        return match.group(4)
    else:
        match = re.search(r'Pickup\s(([\w\d\s]*)Scheduled([\s\d\/\:\-]*);([\w\d\s]*;|)|)(\w*),\s(\w*),\s(\d*)',text)
        if match:
            return match.group(6)
        else:
            match = re.search(r'Pickup\s([\w\s]*), (\w*)(,|.) (\d*)',text)
            if match:
                return match.group(2)
            else:
                match = re.search(r'Pickup\sScheduled\s([\s\d\/\:\-]*);([\w\s]*),\s(\w*),\s(\d*)',text)
                if match:
                    return match.group(3)

# extract postal shipper#
def postal_shipper(text):
    match = re.search(r'Pickup\s([\w\d\s]*)Scheduled[\s\d\/\:\-]*;([\w\d\s]*;|)(\w*),\s(\w*),\s(\d*)', text)
    if match: 
        return match.group(5)
    else:
        match = re.search(r'Pickup\s(([\w\d\s]*)Scheduled([\s\d\/\:\-]*);([\w\d\s]*;|)|)(\w*),\s(\w*),\s(\d*)',text)
        if match:
            return match.group(7)
        else:
            match = re.search(r'Pickup\s([\w\s]*), (\w*)(,|.) (\d*)',text)
            if match:
                return match.group(4)
            else:
                match = re.search(r'Pickup\sScheduled\s([\s\d\/\:\-]*);([\w\s]*),\s(\w*),\s(\d*)',text)
                if match:
                    return match.group(4)
                else:
                    match = re.search(r'Pickup\s([\d\w\s\,]*);([\w\s]*),\s(\d*)',text)
                    if match:
                        return match.group(3)


# extract city Delivery#
def city_drop(text):
    match = re.search(r'Delivery\s([\w\d\s]*)Scheduled[\s\d\/\:\-]*;([\w\d\s]*;|)(\w*),\s(\w*),\s(\d*)', text)
    if match: 
        return match.group(3)
    else:
        
        match = re.search(r'Delivery\s(([\w\d\s]*)Scheduled([\s\d\/\:\-]*);([\w\d\s]*;|)|)(\w*),\s(\w*),\s(\d*)',text)
        if match:
            return match.group(5)
        else:
            match = re.search(r'Delivery\s([\w\s]*), (\w*)(,|.) (\d*)',text)
            if match:
                return match.group(1)
            else:
                match = re.search(r'Delivery\sScheduled\s([\s\d\/\:\-]*);([\w\s]*),\s(\w*),\s(\d*)',text)
                if match:
                    return match.group(2)
                else:
                    match = re.search(r'Delivery\s([\d\w\s\,]*);([\w\s]*),\s(\d*)',text)
                    if match:
                        return match.group(2)

# extract state Delivery#
def state_drop(text):
    match = re.search(r'Delivery\s([\w\d\s]*)Scheduled[\s\d\/\:\-]*;([\w\d\s]*;|)(\w*),\s(\w*),\s(\d*)', text)
    if match: 
        return match.group(4)
    else:
        match = re.search(r'Delivery\s(([\w\d\s]*)Scheduled([\s\d\/\:\-]*);([\w\d\s]*;|)|)(\w*),\s(\w*),\s(\d*)',text)
        if match:
            return match.group(6)
        else:
            match = re.search(r'Delivery\s([\w\s]*), (\w*)(,|.) (\d*)',text)
            if match:
                return match.group(2)
            else:
                match = re.search(r'Delivery\sScheduled\s([\s\d\/\:\-]*);([\w\s]*),\s(\w*),\s(\d*)',text)
                if match:
                    return match.group(3)

# extract postal Delivery#
def postal_drop(text):
    match = re.search(r'Delivery\s([\w\d\s]*)Scheduled[\s\d\/\:\-]*;([\w\d\s]*;|)(\w*),\s(\w*),\s(\d*)', text)
    if match: 
        return match.group(5)
    else:
        match = re.search(r'Delivery\s(([\w\d\s]*)Scheduled([\s\d\/\:\-]*);([\w\d\s]*;|)|)(\w*),\s(\w*),\s(\d*)',text)
        if match:
            return match.group(7)
        else:
            match = re.search(r'Delivery\s([\w\s]*), (\w*)(,|.) (\d*)',text)
            if match:
                return match.group(4)
            else:
                match = re.search(r'Delivery\sScheduled\s([\s\d\/\:\-]*);([\w\s]*),\s(\w*),\s(\d*)',text)
                if match:
                    return match.group(4)
                else:
                    match = re.search(r'Delivery\s([\d\w\s\,]*);([\w\s]*),\s(\d*)',text)
                    if match:
                        return match.group(3)

#extract address shipper
def address_shipper(text):
    match = re.search(r'([\w\d\s\*\;\.]*);1 Pickup', text)
    if match:  
         return match.group(1)
    else:
        return None
#extract address drop
def address_drop(text):
    match = re.search(r'([\w\d\s\*\;\.]*);2 Delivery', text)
    if match:  
         return match.group(1)
    else:
        return None
#extract address broker
def address_broker(text):
    match = re.search(r'Office\s([\w\-\s\,\d]*)', text)
    if match:  
         return match.group(1)
    else:
        return None
#extract phone shipper
def pn_shipper(text):
    match = re.search(r'1 Pickup([\w\d\s\/\-\:\;\,]*)PN:\s*([\d\s\(\)\-]*)', text)
    if match:  
         return match.group(2)
    else:
        return None
#extract phone drop
def pn_drop(text):
    match = re.search(r'2 Delivery([\w\d\s\/\-\:\;\,]*)PN:\s*([\d\s\(\)\-]*)', text)
    if match:  
         return match.group(2)
    else:
        return None
#extract phone broker
def pn_broker(text):
    match = re.search(r'Phone\s([\d\\(\)\s\-]*);Fax', text)
    if match:  
         return match.group(1)
    else:
        return None

            
   
      