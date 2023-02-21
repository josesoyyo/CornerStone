#  kvt_extract_ratecon_werner.py

import re
from functions.get_ratecon_schema import get_rate_confirmation_schema, get_stops_schema, get_entity_schema
from functions.get_ratecon_schema import get_reference_schema, get_note_schema, get_dates_schema, get_purchase_order_schema


def kvt_extract(text):
    """
        :param text : { "0": <STR>,
                        "1": <STR>
                      }
        :return: details = {
                        }
        """

    try:
        
        #  reciever
        def ratecon_receiver(text_doc):
            text_doc = re.sub("\n", " ", text_doc)
            if bool(re.compile(r"(?<=carrier:) +((\S+\s)+)(?=  +)").search(text_doc)):
                receiver = re.compile(r"(?<=carrier:) +((\S+\s)+)(?=  +)").search(text_doc)
                if receiver is not None:
                    receiver = receiver.group(1).upper()
                    if not bool(re.compile(r"\d+").search(receiver)):
                        return receiver        

        #  identifier
        def rate_confirmation_identifier(text_doc):
            text_doc = re.sub("\n", " ", text_doc)
            if bool(re.compile(r"(?<=tour confirmation:) +(\d+)  +").search(text_doc)):
                identifier = re.compile(r"(?<=tour confirmation:) +(\d+)  +").search(text_doc)
                if identifier is not None:
                    identifier = identifier.group(1)
                    return identifier
            elif bool(re.compile(r"(?<=tour #) ?(\d+) ?confirmation").search(text_doc)):
                identifier = re.compile(r"(?<=tour #) ?(\d+) ?confirmation").search(text_doc)
                if identifier is not None:
                    identifier = identifier.group(1)
                    return identifier
            elif bool(re.compile(r"(?<=tour) ?\S+: ?(\d+)  +").search(text_doc)):
                identifier = re.compile(r"(?<=tour) ?\S+: ?(\d+)  +").search(text_doc)
                if identifier is not None:
                    identifier = identifier.group(1)
                    return identifier
            elif bool(re.compile(r"(?<=tour #) ?(\d+) +\S+(?=mation  +)").search(text_doc)):
                identifier = re.compile(r"(?<=tour #) ?(\d+) +\S+(?=mation  +)").search(text_doc)
                if identifier is not None:
                    identifier = identifier.group(1)
                    return identifier        
            else:
                identifier = None
                return identifier        

        #  identifier_type
        def rate_confirmation_identifier_type(text_doc):
            text_doc = re.sub("\n", " ", text_doc)
            if bool(re.compile(r"(?<=tour confirmation:) +(\d+) +").search(text_doc)):
                identifier_type = "TOUR CONFIRMATION"
                return identifier_type
            elif bool(re.compile(r"(?<=tour #) ?(\d+) ?confirmation").search(text_doc)):
                identifier_type = "TOUR CONFIRMATION"
                return identifier_type
            elif bool(re.compile(r"(?<=tour) ?\S+: ?(\d+) +").search(text_doc)):
                identifier_type = "TOUR CONFIRMATION"
                return identifier_type
            elif bool(re.compile(r"(?<=tour #) ?(\d+) +\S+(?=mation +)").search(text_doc)):
                identifier_type = "TOUR CONFIRMATION"
                return identifier_type
            else:
                identifier_type = None
                return identifier_type        

        #  equipment_number
        def rate_confirmation_shipment_equipment_number(text_doc):
            text_doc = re.sub("\n", " ", text_doc)
            if bool(re.compile(r"(?<=equipment #:)\d+").search(text_doc)):
                equipment_number = re.compile(r"(?<=equipment #:)\d+").search(text_doc)
                if equipment_number is not None:
                    equipment_number = equipment_number.group()
                    return equipment_number
            else:
                equipment_number = None
                return equipment_number        

        #  weight
        def rate_confirmation_shipment_weight(text_doc):
            text_doc = re.sub("\n", " ", text_doc)
            wfa_list = []
            if bool(re.compile(r"(?<=weight:)(| | +)(\d+|\d)(| | +)([a-z]{2})(?=.*consignee:)").findall(text_doc)):
                weight_fa = re.compile(r"(?<=weight:)(| | +)(\d+|\d)(| | +)([a-z]{2})(?=.*consignee:)").findall(text_doc)
                if weight_fa is not None:
                    for wf in weight_fa:
                        wfa_list.append(", ")
                        for w in wf:
                            wfa_list.append(w)
                    wfa = "".join(wfa_list)
                    if bool(re.compile(r"\B, ").search(wfa)):
                        wfa = re.sub("\B, ", "", wfa)
                    return wfa  
            else:
                weight = None
                return weight       

        #  weight_unit_code
        def rate_confirmation_shipment_weight_unit_code(text_doc):
            if rate_confirmation_shipment_weight:
                if bool(re.compile(r"lb|lbs|ib|ibs|1b|1bs").search(text_doc)):
                    weight_unit_code = "L"
                    return weight_unit_code
                elif bool(re.compile(r"kg|kgs").search(text_doc)):
                    weight_unit_code = "K" 
                    return weight_unit_code       

        # volume 
        def rate_confirmation_shipment_volume(text_doc):
            text_doc = re.sub("\n", " ", text_doc)
            if bool(re.compile(r"(?<=cube:) ?(\d+.\d+) ?(\S+ \S+) +").search(text_doc)):
                volume_str = re.compile(r"(?<=cube:) ?(\d+.\d+) ?(\S+ \S+) +").search(text_doc)
                if volume_str is not None:
                    volume = volume_str.group(1)
                    return volume
            else:
                volume = None
                return volume

        # volume_qualifier
        def rate_confirmation_shipment_volume_qualifier(text_doc):
            text_doc = re.sub("\n", " ", text_doc)
            if bool(re.compile(r"(?<=cube:) ?(\d+.\d+) ?(\S+ \S+)  +").search(text_doc)):
                volume_str = re.compile(r"(?<=cube:) ?(\d+.\d+) ?(\S+ \S+)  +").search(text_doc)
                if volume_str is not None:
                    volume_qualifier = volume_str.group(2)
                    return volume_qualifier
            else:
                volume_qualifier = None
                return volume_qualifier    

        #  truck_type
        def rate_confirmation_shipment_truck_type(text_doc):
            text_doc = re.sub("\n", " ", text_doc)
            if bool(re.compile(r"(?<=equipment:) ?(\S+) ?(?=equipment #| +)").search(text_doc)):
                truck = re.compile(r"(?<=equipment:) ?(\S+) ?(?=equipment #| +)").search(text_doc)
                if truck is not None:
                    truck_type = truck.group(1)
                    return truck_type
            else:
                truck_type = None
                return truck_type    

        #  charges
        def rate_confirmation_shipment_charges(text_doc):
            if bool(re.compile(r"(?<=total charges:)(| | +)(\$?\d+,\d+.\d+|\$?\d,\d+.\d+|\$?\d+.\d+)").search(text_doc)):
                total_charges = re.compile(r"(?<=total charges:)(| | +)(\$?\d+,\d+.\d+|\$?\d,\d+.\d+|\$?\d+.\d+)").search(text_doc)
                if total_charges is not None:
                    charges = total_charges.group(2)
                    return charges
            else:
                charges = None
                return charges

        #  loading_quantity
        def rate_confirmation_shipment_loading_quantity(text_doc):
            if bool(re.compile(r"(?<=quantity:) ?(\d+ ?\S+?) +(?=weight:)").search(text_doc)):
                qty = re.compile(r"(?<=quantity:) ?(\d+ ?\S+?) +(?=weight:)").search(text_doc)
                if qty is not None:
                    loading_quantity = qty.group(1)
                    return loading_quantity
            else:
                loading_quantity = None
                return loading_quantity    

        #  dates
        def rate_confirmation_dates(text_doc):
            date_dict = get_dates_schema()
            if bool(re.compile(r"(?<=printed:)(| | +)(\d{2})/(\d{2})/(\d{4}) (\d{1,2}:\d{2})").search(text_doc)):
                doc_date_str = re.compile(r"(?<=printed:)(| | +)(\d{2})/(\d{2})/(\d{4}) (\d{1,2}:\d{2})").search(text_doc)
                if doc_date_str is not None:
                    year = doc_date_str.group(4)
                    month = doc_date_str.group(2)
                    day = doc_date_str.group(3)
                    time = doc_date_str.group(5)
                    doc_date = year+"-"+month+"-"+day
                    date_dict.update({"date": doc_date})
                    date_dict.update({"datetype": "PRINTED"})
                    date_dict.update({"time": time})
                    date_dict.update({"timetype": "PRINTED"})                
                    return date_dict
            else:
                date_dict = None
                return date_dict
            
        #  client
        def ratecon_client(text_doc):
            text_doc = re.sub("\n", " ", text_doc)
            if bool(re.compile(r"(?<=office:) +(\S(\S+\s)+)").search(text_doc)):
                name = re.compile(r"(?<=office:) +(\S(\S+\s)+)").search(text_doc)
                if name is not None:
                    name = name.group(1)
                    if not bool(re.compile(r"\d+ [a-z]").search(name)):  # if "address" is NOT and address
                        if not bool(re.compile(r":|phone|office|rd").search(name)):
                            client = name.upper()
                            return client
                    else:
                        client = "WERNER LOGISTICS"
                        return client                        
            else:
                client = "WERNER LOGISTICS"
                return client

        # FOR RATECON LEVEL INFO, ALL BEFORE "SHIPPER:"
        def ratecon_references_blob(text_doc):
            if bool(re.compile(r"(?<!\d)1/2(?!\d)").search(text_doc)):
                blob1 = re.compile(r"([\w\s\n\D]+)(?=(?<!\d)1/2(?!\d))").search(text_doc)
                if blob1 is not None:
                    blob1_ = blob1.group()
                    blob_ = bool(re.compile(r"([\w\s\n\D]+)(?=shipper:.*appt type:)").search(blob1_))
                    if blob_:
                        blob = re.compile(r"([\w\s\n\D]+)(?=shipper:.*appt type:)").search(blob1_)
                        if blob is not None:
                            blob = blob.group()
                            blob = re.sub("\n", " ", blob)
                            return blob
            elif not bool(re.compile(r"(?<!\d)1/2(?!\d)").search(text_doc)):    
                blob_ = bool(re.compile(r"([\w\s\n\D]+)(?=shipper:.*appt type:)").search(text_doc))
                if blob_:
                    blob = re.compile(r"([\w\s\n\D]+)(?=shipper:.*appt type:)").search(text_doc)
                    if blob is not None:
                        blob = blob.group()
                        blob = re.sub("\n", " ", blob)
                        return blob    
                    
        #  ENTITIES:: BROKER BLOB
        def entities_broker_blob(text_doc):  # feeds info blob into entities_broker_extract()
            if bool(re.compile(r"(?<!\d)1/2(?!\d)").search(text_doc)):
                blob1 = re.compile(r"([\w\s\n\D]+)(?=(?<!\d)1/2(?!\d))").search(text_doc)
                if blob1 is not None:
                    blob1 = blob1.group()
                    entities_blob_ = bool(re.compile(r"([\w\s\n\D]+)(?=this form must be signed)").search(blob1))
                    if entities_blob_:
                        entities_blob = re.compile(r"([\w\s\n\D]+)(?=this form must be signed)").search(blob1)
                        if entities_blob is not None:
                            entities_blob = entities_blob.group()
                            entities_blob = re.sub("\n", " ", entities_blob)
                            return entities_blob
            elif not bool(re.compile(r"(?<!\d)1/2(?!\d)").search(text_doc)):
                entities_blob_ = bool(re.compile(r"([\w\s\n\D]+)(?=this form must be signed)").search(text_doc))
                if entities_blob_:
                    entities_blob = re.compile(r"([\w\s\n\D]+)(?=this form must be signed)").search(text_doc)
                    if entities_blob is not None:
                        entities_blob = entities_blob.group()
                        entities_blob = re.sub("\n", " ", entities_blob)
                        return entities_blob
                    
        # STOP BLOBS (returns list of stops with each stop as a dictionary)
        def stop_blobs(text_doc):  # all stops after shipper=consignee
            text_doc = re.sub("\n", "     ", text_doc)
            text_doc = re.sub("\xad|\\t", " ", text_doc)
            pickup_count = 0
            drop_count = 0
            stop_count = 0
            all_stops = []  # append pick_list, then drop_list. pickups = [0], drops = [1]
            pick_list = []  # append first to all_stops
            drop_list = []  # append second to all_stops
            # make sure that we aren't looking at duplicated pages
            if bool(re.compile(r".*(?<!\d)1/2(?!\d).*").search(text_doc)):
                t2_ = re.compile(r"(?<!\d)1/2(?!\d).*").search(text_doc)  # extract page 2
                if t2_ is not None:
                    t2 = t2_.group()
                    if not bool(re.compile(r"stop:|consignee:").search(t2)):  # make sure there aren't stops on page 2
                        t = re.compile(r".*(?<!\d)1/2(?!\d)").search(text_doc)
                        if t is not None:
                            text_doc = t.group()  # output newly sliced text_doc string variable
            # start our count with "shipper"        
            if bool(re.compile(r"shipper:").search(text_doc)):  # change to "stop {number}" to make it easy
                stop_count += 1
                pickup_count += 1
                text_doc = re.sub("shipper:", f"stop {stop_count}::shipper::", text_doc, count=1)
            if bool(re.compile(r"stop:(?=.*consignee)").findall(text_doc)):  # count stops before "consignee" (if any)
                stps = re.compile(r"stop:(?=.*consignee)").findall(text_doc)
                if stps is not None:
                    for s in stps:
                        stop_count += 1
                        drop_count += 1
                        text_doc = re.sub("stop:", f"stop {stop_count}::", text_doc, count=1)
            if bool(re.compile(r"consignee:").search(text_doc)):  # change "consignee" to "stop {number}::consignee" to make it easy
                stop_count += 1
                drop_count += 1
                text_doc = re.sub("consignee:", f"stop {stop_count}::consignee::", text_doc, count=1)  # change to "stop {number}" to make it easy
            if bool(re.compile(r"(?<=consignee).*(stop:)").findall(text_doc)):  # count "stops" after "consignee" (if any)
                stps = re.compile(r"(?<=consignee).*(stop:)").findall(text_doc)
                if stps is not None:
                    for s in stps:
                        stop_count += 1
                        drop_count += 1
                        text_doc = re.sub("stop:", f"stop {stop_count}::", text_doc, count=1)
            if pickup_count >= 1 and drop_count >= 1:
                pick_range = range(1, pickup_count + 1)
                drop_range = range(1, drop_count + 1)
                ordinal = 1
                for i in pick_range:
                    next_stop = ordinal + 1
                    if bool(re.compile(fr"(?<=stop) {ordinal}::.*(?=stop {next_stop}::)").search(text_doc)):
                        ship_ = re.compile(fr"(?<=stop) {ordinal}::.*(?=stop {next_stop}::)").search(text_doc)
                        if ship_ is not None:
                            ship = ship_.group()
                            p_dict = {ordinal: ship}
                            pick_list.append(p_dict)
                            ordinal += 1
                for i in drop_range:
                    next_stop = ordinal + 1
                    if bool(re.compile(fr"(?<=stop) {ordinal}::.*(?=stop {next_stop}::)").search(text_doc)):
                        stop_ = re.compile(fr"(?<=stop) {ordinal}::.*(?=stop {next_stop}::)").search(text_doc)
                        if stop_ is not None:
                            stop = stop_.group()
                            p_dict = {ordinal: stop}
                            if not bool(re.compile(r"p/u|pick(|-| )up").search(stop)):
                                drop_list.append(p_dict)
                            elif bool(re.compile(r"p/u|pick(|-| )up").search(stop)):
                                pick_list.append(p_dict)
                            ordinal += 1
                    elif bool(re.compile(fr"(?<=stop) {ordinal}::.*(?=submit freight bill to:|bill to:)").search(text_doc)):
                        stop_ = re.compile(fr"(?<=stop) {ordinal}::.*(?=submit freight bill to:|bill to:)").search(text_doc)
                        if stop_ is not None:
                            stop = stop_.group()
                            p_dict = {ordinal: stop}
                            drop_list.append(p_dict)
                            ordinal += 1 
                    elif bool(re.compile(fr"(?<=stop) {ordinal}::.*(?=attn:|https)").search(text_doc)):
                        stop_ = re.compile(fr"(?<=stop) {ordinal}::.*(?=attn:|https)").search(text_doc)
                        if stop_ is not None:
                            stop = stop_.group()
                            p_dict = {ordinal: stop}
                            drop_list.append(p_dict)
                            ordinal += 1 
                all_stops.append(pick_list)
                all_stops.append(drop_list)
                return all_stops
                    
        # EXTRACTS REFERENCES FOR ANY TEXT BLOB
        def references_extract(text_blob):
            if text_blob:
                blob = text_blob
                if bool(re.compile(r"(?<=po)  +(?=number:)").search(blob)):
                    blob = re.sub("(?<=po)  +(?=number:)", "po number:", blob)        
                blob = re.sub("(?<=:) +", " ", blob)  
                references_list = []
                if bool(re.compile(r"(?<=gl acct num)(| +)(\d+)").search(blob)):
                    ref_id = re.compile(r"(?<=gl acct num)(| +)(\d+)").findall(blob)
                    ref_list = []
                    if ref_id is not None:
                        for i in ref_id:
                            ref_ = re.compile(r"(\d+)").search(str(i))
                            if ref_ is not None:
                                ref_ = ref_.group()
                                if ref_ not in ref_list:
                                    ref_list.append(ref_)
                        for ref in ref_list:
                            references_dict = get_reference_schema()
                            references_dict.update({"id": f"{ref}", "idtype": "4F", "_idtype": "GL ACCOUNT NUMBER"})
                            references_list.append(references_dict)       
                if bool(re.compile(r"(?<=po number:)(| | +)([a-z0-9\-?]+)").search(blob)):
                    ref_id2 = re.compile(r"(?<=po number:)(| | +)(a-z0-9\-?]+|\d+)").findall(blob)
                    ref_list = []
                    if ref_id2 is not None:
                        for i in ref_id2:
                            ref_ = re.compile(r"([a-z0-9\-?]+)").search(str(i))
                            if ref_ is not None:
                                ref_ = ref_.group()
                                if ref_ not in ref_list:
                                    ref_list.append(ref_)
                        for ref in ref_list:
                            references_dict = get_reference_schema()
                            references_dict.update({"id": f"{ref}", "idtype": "PO", "_idtype": "PO NUMBER"})
                            references_list.append(references_dict)                      
                if bool(re.compile(r"(?<=bill of lading:)(| | +)([a-z0-9\-?]+)").search(blob)):
                    ref_id3 = re.compile(r"(?<=bill of lading:)(| | +)([a-z0-9\-?]+|\d+)").findall(blob)
                    ref_list = []
                    if ref_id3 is not None:
                        for i in ref_id3:
                            ref_ = re.compile(r"([a-z0-9\-?]+|\d+)").search(str(i))
                            if ref_ is not None:
                                ref_ = ref_.group()
                                if ref_ not in ref_list:
                                    ref_list.append(ref_)
                        for ref in ref_list:
                            references_dict = get_reference_schema()
                            references_dict.update({"id": f"{ref}", "idtype": "BM", "_idtype": "BILL OF LADING"})
                            references_list.append(references_dict)                
                if bool(re.compile(r"(?<=shipper reference #:)(| | +)([a-z0-9\-?]+)").search(blob)):
                    ref_id4 = re.compile(r"(?<=shipper reference #:)(| | +)([a-z0-9\-?]+|\d+)").findall(blob)
                    ref_list = []
                    if ref_id4 is not None:
                        for i in ref_id4:
                            ref_ = re.compile(r"[a-z0-9]+").search(str(i))
                            if ref_ is not None:
                                ref_ = ref_.group()
                                if ref_ not in ref_list:
                                    ref_list.append(ref_)
                        for ref in ref_list:
                            references_dict = get_reference_schema()
                            references_dict.update({"id": f"{ref}", "idtype": "AI", "_idtype": "SHIPPER REFERENCE"})
                            references_list.append(references_dict)
                if bool(re.compile(r"(?<=pickup number:)(| | +)([a-z0-9\-?]+)").search(blob)):
                    ref_id5 = re.compile(r"(?<=pickup number:)(| | +)([a-z0-9\-?]+|\d+)").findall(blob)
                    ref_list = []
                    if ref_id5 is not None:
                        for i in ref_id5:
                            ref_ = re.compile(r"([a-z0-9\-?]+|\d+)").search(str(i))
                            if ref_ is not None:
                                ref_ = ref_.group()
                                if ref_ not in ref_list:
                                    ref_list.append(ref_)
                        for ref in ref_list:
                            references_dict = get_reference_schema()
                            references_dict.update({"id": f"{ref}", "idtype": "PUA", "_idtype": "PICKUP NUMBER"})
                            references_list.append(references_dict)                
                if bool(re.compile(r"(?<=load id #:)(| | +)([a-z0-9\-?]+)").search(blob)):
                    ref_id6 = re.compile(r"(?<=load id #:)(| | +)([a-z0-9\-?]+|\d+)").findall(blob)
                    ref_list = []
                    if ref_id6 is not None:
                        for i in ref_id6:
                            ref_ = re.compile(r"([a-z0-9\-?]+|\d+)").search(str(i))
                            if ref_ is not None:
                                ref_ = ref_.group()
                                if ref_ not in ref_list:
                                    ref_list.append(ref_)
                        for ref in ref_list:
                            references_dict = get_reference_schema()
                            references_dict.update({"id": f"{ref}", "idtype": "Y5", "_idtype": "LOAD ID"})
                            references_list.append(references_dict) 
                if bool(re.compile(r"(?<=pu appt #:)(| | +)([a-z0-9\-?]+)").search(blob)):
                    ref_id7 = re.compile(r"(?<=pu appt #:)(| | +)([a-z0-9\-?]+|\d+)").findall(blob)
                    ref_list = []
                    if ref_id7 is not None:
                        for i in ref_id7:
                            ref_ = re.compile(r"([a-z0-9\-?]+)").search(str(i))
                            if ref_ is not None:
                                ref_ = ref_.group()
                                if ref_ not in ref_list:
                                    ref_list.append(ref_)
                        for ref in ref_list:
                            references_dict = get_reference_schema()
                            references_dict.update({"id": f"{ref}", "idtype": "PUA", "_idtype": "PU APPOINTMENT"})
                            references_list.append(references_dict)    
                if bool(re.compile(r"(?<=carrier reference #:)(| | +)([a-z0-9\-?]+)").search(blob)):
                    ref_id8 = re.compile(r"(?<=carrier reference #:)(| | +)([a-z0-9\-?]+|\d+)").findall(blob)
                    ref_list = []
                    if ref_id8 is not None:
                        for i in ref_id8:
                            ref_ = re.compile(r"([a-z0-9\-?]+)").search(str(i))
                            if ref_ is not None:
                                ref_ = ref_.group()
                                if ref_ not in ref_list:
                                    ref_list.append(ref_)
                        for ref in ref_list:
                            references_dict = get_reference_schema()
                            references_dict.update({"id": f"{ref}", "idtype": "CR", "_idtype": "CARRIER REFERENCE"})
                            references_list.append(references_dict)
                if bool(re.compile(r"(?<=manifest number:)(| | +)([a-z0-9\-?]+)").search(blob)):
                    ref_id9 = re.compile(r"(?<=manifest number:)(| | +)([a-z0-9\-?]+)").findall(blob)
                    ref_list = []
                    if ref_id9 is not None:
                        for i in ref_id9:
                            ref_ = re.compile(r"([a-z0-9\-?]+])").search(str(i))
                            if ref_ is not None:
                                ref_ = ref_.group()
                                if ref_ not in ref_list:
                                    ref_list.append(ref_)
                        for ref in ref_list:
                            references_dict = get_reference_schema()
                            references_dict.update({"id": f"{ref}", "idtype": "Y5", "_idtype": "MANIFEST NUMBER"})
                            references_list.append(references_dict)  
                if bool(re.compile(r"(?<=del appt #:)(| | +)([a-z0-9\-?]+)").search(blob)):
                    ref_id9 = re.compile(r"(?<=del appt #:)(| | +)([a-z0-9\-?]+|\d+)").findall(blob)
                    ref_list = []
                    if ref_id9 is not None:
                        for i in ref_id9:
                            ref_ = re.compile(r"([a-z0-9\-?]+)").search(str(i))
                            if ref_ is not None:
                                ref_ = ref_.group()
                                if ref_ not in ref_list:
                                    ref_list.append(ref_)
                        for ref in ref_list:
                            references_dict = get_reference_schema()
                            references_dict.update({"id": f"{ref}", "idtype": "DAN", "_idtype": "DEL APPT"})
                            references_list.append(references_dict)  
                return references_list                    
                    
        # FOR EXTRACTING STOP ENTITY INFO, FEED INTO full_stop_data_extract(stop_type, text_blob_dict)
        def stop_entity_data_extract(stop_type, text_blob_dict):
            blob = text_blob_dict
            entity_dict = get_entity_schema("SHIPPER")  # only here to keep PyCharm happy, redefined below
            if stop_type.upper() == "PICK":
                entity_dict = get_entity_schema("SHIPPER")   
                entity_dict.update({"_type": "SH", "id": "10", "idtype": "MUTUALLY DEFINED", "_idtype": "ZZ"})
            elif stop_type.upper() == "DROP":
                entity_dict = get_entity_schema("CONSIGNEE")   
                entity_dict.update({"_type": "CN", "id": "10", "idtype": "MUTUALLY DEFINED", "_idtype": "ZZ"})
            if stop_type.upper() == "PICK" or stop_type.upper() == "DROP":
                for num, text_ in blob.items():
                    # name
                    if bool(re.compile(r"(?<=::)([\w\s()]+)(?=appt type:)").search(text_)): 
                        name_ = re.compile(r"(?<=::)([\w\s()]+)(?=appt type:)").search(text_)
                        if name_ is not None:
                            name = name_.group()
                            if bool(re.compile(r" +").search(name)):
                                name = re.sub(" +", " ", name)
                            entity_dict.update({"name": name.upper()})
                    # street address        
                    if bool(re.compile(r"(?<=appointment)  +([0-9]+ [a-z0-9.? -?]+)  +(?=date/time:)|(?<=appointment)  +([a-z0-9.? -?]+ [0-9]+)  +(?=date/time:)").search(text_)):
                        add_ = re.compile(r"(?<=appointment)  +([0-9]+ [a-z0-9.? -?]+)  +(?=date/time:)|(?<=appointment)  +([a-z0-9.? -?]+ [0-9]+)  +(?=date/time:)").search(text_)
                        if add_ is not None:
                            address = add_.group()
                            if bool(re.compile(r" +").search(address)):
                                address = re.sub(" +", " ", address)
                            entity_dict["address"].append(address.upper())
                    # street address alternative            
                    elif bool(re.compile(r"(?<=window)  +([0-9]+ [a-z0-9.? -?]+)  +(?=earliest date/time:)|(?<=window)  +([a-z0-9.? -?]+ [0-9]+)  +(?=earliest date/time:)").search(text_)):
                        add_ = re.compile(r"(?<=window)  +([0-9]+ [a-z0-9.? -?]+)  +(?=earliest date/time:)|(?<=window)  +([a-z0-9.? -?]+ [0-9]+)  +(?=earliest date/time:)").search(text_)
                        if add_ is not None:
                            address = add_.group()
                            if bool(re.compile(r" +").search(address)):
                                address = re.sub(" +", " ", address)
                            entity_dict["address"].append(address.upper())
                    # check where city, state zipcode is supposed to be first before looking for street address 2      
                    if not bool(re.compile(r"(?<=\d{4} \d{2}:\d{2})  +(([a-z. ]+ )?[a-z]+), ([a-z]{2}) (\d+)  +(?=miles:(?! for load))").search(text_)):                
                        # city, state, zipcode
                        if bool(re.compile(r"(?<=miles:)  +[0-9.]+   +(([a-z. ]+ )?[a-z]+), ([a-z]{2}) (\d+)  +").search(text_)):
                            c_s_z = re.compile(r"(?<=miles:)  +[0-9.]+   +(([a-z. ]+ )?[a-z]+), ([a-z]{2}) (\d+)  +").search(text_)
                            if c_s_z is not None:
                                city = c_s_z.group(1).upper()
                                state = c_s_z.group(3).upper()
                                zipcode = c_s_z.group(4)
                                entity_dict.update({"city": city, "state": state, "postal": zipcode, "country": "USA"})
                                # address 2
                                if bool(re.compile(r"(?<=\d{4} \d{2}:\d{2})  +([a-z 0-9]+)  +(?=miles:)").search(text_)):  # address 2
                                    add_2 = re.compile(r"(?<=\d{4} \d{2}:\d{2})  +([a-z 0-9]+)  +(?=miles:)").search(text_)
                                    if add_2 is not None:
                                        add2 = add_2.group(0)
                                        if bool(re.compile(r" +").search(add2)):
                                            add2 = re.sub(" +", " ", add2)
                                        entity_dict["address"].append(add2.upper()) 
                    # city, state, zip (if there is no street address 2)                    
                    if bool(re.compile(r"(?<=\d{4} \d{2}:\d{2})  +(([a-z. ]+ )?[a-z]+), ([a-z]{2}) (\d+)  +(?=miles:(?! for load))").search(text_)):
                        c_s_z = re.compile(r"(?<=\d{4} \d{2}:\d{2})  +(([a-z. ]+ )?[a-z]+), ([a-z]{2}) (\d+)  +(?=miles:(?! for load))").search(text_)
                        if c_s_z is not None:
                            city = c_s_z.group(1).upper()
                            state = c_s_z.group(3).upper()
                            zipcode = c_s_z.group(4).upper()                    
                            entity_dict.update({"city": city, "state": state, "postal": zipcode, "country": "USA"})
                    # city, state, zip (if there is no street address 2) -- alternative 
                    elif bool(re.compile(r"(?<=\d{4} \d{2}:\d{2})  +(([a-z. ]+ )?[a-z]+), ([a-z]{2}) (\d+)  +(?=latest date/time:)").search(text_)):
                        c_s_z = re.compile(r"(?<=\d{4} \d{2}:\d{2})  +(([a-z. ]+ )?[a-z]+), ([a-z]{2}) (\d+)  +(?=latest date/time:)").search(text_)
                        if c_s_z is not None:
                            city = c_s_z.group(1).upper()
                            state = c_s_z.group(3).upper()
                            zipcode = c_s_z.group(4).upper()                    
                            entity_dict.update({"city": city, "state": state, "postal": zipcode, "country": "USA"})
                    if bool(re.compile(r"(([a-z]+ )?[a-z]+) ?:? ?[(]?\d{3}[) -]\d{3}[ -]\d{4}").search(text_)):
                        c_num_ = re.compile(r"(([a-z]+ )?[a-z]+) ?:? ?[(]?(\d{3})[) -](\d{3})[ -](\d{4})").search(text_)
                        if c_num_ is not None:
                            c = c_num_.group(1)
                            number = c_num_.group(3)+"-"+c_num_.group(4)+"-"+c_num_.group(5)
                            entity_dict["contacts"].update({"contactname": c, "contact_type": "REP", "contact_number": number, "contact_number_type": "PHONE"})
                return entity_dict                     
                    
        #  Universal NOTES/COMMENTS
        def universal_notes_extract(blob_type, text_doc):
            notes_dict = get_note_schema()
            blob = text_doc
            if blob_type.upper() == "RATECON":
                blob = ratecon_references_blob(text_doc)
                notes_dict.update({"notetype": "RATECON-LEVEL COMMENTS", "_notetype": "RATECON NOTES"})
            if blob_type.upper() == "SHIPPER":
                notes_dict.update({"notetype": "SHIPPER COMMENTS", "_notetype": "PICK NOTES"})
            if blob_type.upper() == "CONSIGNEE":
                notes_dict.update({"notetype": "CONSIGNEE COMMENTS", "_notetype": "DROP NOTES"})
            if blob is not None:
                if bool(re.compile(r"(?<=comments:).*").search(blob)):
                    blob_ = re.compile(r"(?<=comments:).*").search(blob)
                    if blob_ is not None:
                        blob = blob_.group()
                if bool(re.compile(r".*commodity:").search(blob)):
                    blob_ = re.compile(r".*(?=commodity:)").search(blob)
                    if blob_ is not None:
                        blob = blob_.group()
                if bool(re.compile(r"# :|#:").search(blob)):
                    blob = re.sub("# :|#:", ":", blob)
                if bool(re.compile(r"(?<=:) +(?=\d+)").search(blob)):
                    blob = re.sub("(?<=:) +(?=\d+)", "", blob)   
                if bool(re.compile(r"([a-z]+ )?([a-z]+ )?[a-z]+ ?: ?([a-z0-9-]+|  +)").search(blob)):
                    blob = re.sub("([a-z]+ )?([a-z]+ )?[a-z]+ ?: ?([a-z0-9-]+|  +)", "", blob)  
                blob = re.sub(" +", " ", blob)
                # print(f"post-edit-blob:::\n{blob}\n\n")
                notes_dict.update({"note": f"{blob}"})
                return notes_dict                   
                    
        # FOR EXTRACTING ENTITY/NOTES/REFERENCES/STOP_DETAIL INFO FROM STOPS
        def full_stop_data_extract(stop_type, text_blob_dict):
            blob = text_blob_dict
            stop_dict = get_stops_schema("PICK", 1)  # only here to keep PyCharm happy, redefined below
            if stop_type.upper() == "PICK":
                for num, text in blob.items():
                    stop_dict = get_stops_schema("PICK", int(num))
                    if stop_entity_data_extract("PICK", blob):
                        if stop_entity_data_extract("PICK", blob) not in stop_dict["entities"]:
                            stop_dict["entities"].append(stop_entity_data_extract("PICK", blob))
                    blob = text
                    if universal_notes_extract("SHIPPER", blob):  # stop notes extract
                        stop_dict["notes"].append(universal_notes_extract("SHIPPER", blob))
                    if references_extract(blob):
                        refs = references_extract(blob)
                        for ref in refs:
                            stop_dict["references"].append(ref)  # stop references extract
            elif stop_type.upper() == "DROP":
                for num, text in blob.items():
                    stop_dict = get_stops_schema("DROP", int(num))
                    if stop_entity_data_extract("DROP", blob):
                        if stop_entity_data_extract("DROP", blob) not in stop_dict["entities"]:
                            stop_dict["entities"].append(stop_entity_data_extract("DROP", blob))
                    blob = text
                    if universal_notes_extract("CONSIGNEE", blob):  # stop notes extract
                        stop_dict["notes"].append(universal_notes_extract("CONSIGNEE", blob))
                    if references_extract(blob):
                        refs = references_extract(blob)
                        for ref in refs:
                            stop_dict["references"].append(ref)  # stop references extract
            if stop_type.upper() == "PICK" or stop_type.upper() == "DROP":
                # earliest stop-level date
                if bool(re.compile(r"(?<=earliest date/time:)(| | +)(\d{2})/(\d{2})/(\d{4}) ?(\d{2}:\d{2})").search(blob)):  # earliest date/time
                    date_time_1 = re.compile(r"(?<=earliest date/time:)(| | +)(\d{2})/(\d{2})/(\d{4}) ?(\d{2}:\d{2})").search(blob)
                    if date_time_1 is not None:    
                        year = date_time_1.group(4)
                        month = date_time_1.group(2)
                        day = date_time_1.group(3)
                        if len(day) == 1:
                            day = "0"+day
                        time = date_time_1.group(5)
                        date = year+"-"+month+"-"+day
                        dates_dict = get_dates_schema()
                        dates_dict.update({"date": f"{date}", "datetype": "EP", "time": f"{time}", "timetype": "EARLIEST"})
                        stop_dict["dates"].append(dates_dict)
                # earliest stop-level date (alternative)        
                elif bool(re.compile(r"(?<=date/time:)(| | +)(\d{2})/(\d{2})/(\d{4}) ?(\d{2}:\d{2})").search(blob)):
                    date_time_1_2 = re.compile(r"(?<=date/time:)(| | +)(\d{2})/(\d{2})/(\d{4}) ?(\d{2}:\d{2})").search(blob)
                    if date_time_1_2 is not None:
                        year = date_time_1_2.group(4)
                        month = date_time_1_2.group(2)
                        day = date_time_1_2.group(3)
                        if len(day) == 1:
                            day = "0"+day
                        time = date_time_1_2.group(5)
                        date = year+"-"+month+"-"+day
                        dates_dict = get_dates_schema()
                        dates_dict.update({"date": f"{date}", "datetype": "EP", "time": f"{time}", "timetype": "EARLIEST"})
                        stop_dict["dates"].append(dates_dict)                
                # latest stop-level date        
                if bool(re.compile(r"(?<=latest date/time:)(| | +)(\d{1,2})/(\d{2})/(\d{4}) ?(\d{2}:\d{2})").search(blob)):  # latest date/time
                    date_time_2 = re.compile(r"(?<=latest date/time:)(| | +)(\d{1,2})/(\d{2})/(\d{4}) ?(\d{2}:\d{2})").search(blob)
                    if date_time_2 is not None:
                        year = date_time_2.group(4)
                        month = date_time_2.group(2)
                        day = date_time_2.group(3)
                        if len(day) == 1:
                            day = "0"+day
                        time = date_time_2.group(5)
                        date = year+"-"+month+"-"+day
                        dates_dict = get_dates_schema()
                        dates_dict.update({"date": f"{date}", "datetype": "LP", "time": f"{time}", "timetype": "LATEST"})
                        stop_dict["dates"].append(dates_dict)
                po_dict = get_purchase_order_schema()   
                # weight         
                if bool(re.compile(r"(?<=weight:)(| | +)(\d+|\d)(| | +)([a-z]{2})").search(blob)):
                    wt_ = re.compile(r"(?<=weight:)(| | +)(\d+|\d)(| | +)([a-z]{2})").search(blob)
                    if wt_ is not None:
                        wt = wt_.group(2)
                        po_dict.update({"weight": wt})
                        if bool(re.compile(r"lb|lbs|ib|ibs|1b|1bs").search(wt_.group(0))):
                            po_dict.update({"weight_unit_code": "L"})
                        elif bool(re.compile(r"kg|k8").search(wt_.group(0))):
                            po_dict.update({"weight_unit_code": "K"})
                # po number        
                if bool(re.compile(r"(?<=po number:)(| | +)([a-z0-9\-?]+)").search(blob)):
                    ponum_ = re.compile(r"(?<=po number:)(| | +)(a-z0-9\-?]+|\d+)").findall(blob)
                    ponum_list = []
                    if ponum_ is not None:
                        for i in ponum_:
                            po_ = re.compile(r"([a-z0-9\-?]+)").search(str(i))
                            if po_ is not None:
                                po_ = po_.group()
                                if po_ not in ponum_list:
                                    ponum_list.append(po_)
                                po = " ".join(ponum_list)
                                if po is not None:
                                    po_dict.update({"purchase_order_number": po})
                # po number (alternative (shipper-reference))       
                elif bool(re.compile(r"(?<=shipper reference #:)(| | +)([a-z0-9\-?]+)").search(blob)):
                    ponum_ = re.compile(r"(?<=shipper reference #:)(| | +)([a-z0-9\-?]+)").findall(blob)
                    ponum_list = []
                    if ponum_ is not None:
                        for i in ponum_:
                            po_ = re.compile(r"([a-z0-9\-?]+)").search(str(i))
                            if po_ is not None:
                                po_ = po_.group()
                                if po_ not in ponum_list:
                                    ponum_list.append(po_)
                                po = " ".join(ponum_list)
                                if po is not None:
                                    po_dict.update({"purchase_order_number": po})
                if po_dict["purchase_order_number"] is not None or po_dict["weight"] is not None or po_dict["cases"] is not None:               
                    stop_dict["order_detail"][0]["purchase_order_number"].append(po_dict) 

                return stop_dict                    

        #  ENTITIES:"BROKER" EXTRACT`
        def entities_broker_extract(text_doc):  # address, city, state, country, postal
            state_abbrev = " al | ak | az | ar | ca | co | ct | de | fl | ga | hi | id | il | in | ia | ks | ky | la | me | md \
            | ma | mi | mn | ms | mo | mt | ne | nv | nh | nj | nm | ny | nc | nd | oh | ok | or | pa | ri | sc | sd | tn | tx \
            | tx | ut | vt | va | wa | wv | wi | wy "
            entity_dict = get_entity_schema("BROKER")
            #  name     
            if bool(re.compile(r"werner").search(text_doc)):
                if ratecon_client(text_doc):
                    entity_dict.update({"name": f"{ratecon_client(text_doc)}"})
                else:
                    entity_dict.update({"name": "WERNER LOGISTICS"})
                entity_dict.update({"_type": "BK", "id": "10", "idtype": "MUTUALLY DEFINED", "_idtype": "ZZ"})    
                if entities_broker_blob(text_doc):
                    blob = entities_broker_blob(text_doc)
                    blob = re.sub("\n", " ", blob)
                    #  "office" address (NO city/state/zipcode)    
                    if bool(re.compile(r"(?<=office:) +([0-9]+ [a-z]+ [a-z]+)+").search(blob)):
                        address = re.compile(r"(?<=office:) +([0-9]+ [a-z]+ [a-z]+)+").search(blob)
                        if address is not None:
                            address = address.group(1)
                            # check to make sure "address" is an address, could be name of a different brokerage 
                            if bool(re.compile(r"\d+ \D").search(address)):  # if "address" is NOT and address
                                address = [address.upper()]
                                entity_dict.update({"address": f"{address}"})

                    #  contact_number, contact_number_type (PHONE)      
                    if bool(re.compile(r"(?<=phone:) +([ (]\d{3}[). -] ?\d{3}[. -]\d{4})(?!.*after 5pm)").search(blob)):
                        contact_phone = re.compile(r"(?<=phone:) +([ (]\d{3}[). -] ?\d{3}[. -]\d{4})(?!.*after 5pm)").search(blob)
                        if contact_phone is not None:
                            contact_phone = contact_phone.group(1)
                            contact_number_type = "PHONE"
                            entity_dict["contacts"].update({"contact_number": f"{contact_phone}", "contact_number_type": f"{contact_number_type}"})
                    #  contactname, contact_type
                    blob = re.sub("(?<=:) +", " ", blob)
                    if bool(re.compile(r"(?<=contact:) (([a-z]+ )?[a-z]+)").search(blob)):
                        contact_name = re.compile(r"(?<=contact:) (([a-z]+ )?[a-z]+)").search(blob)
                        if contact_name is not None:
                            contactname = contact_name.group(1).upper()
                            contact_type = "BROKER REP"
                            entity_dict["contacts"].update({"contactname": f"{contactname}", "contact_type": f"{contact_type}"}) 
                return entity_dict                    
                    
        #  data extraction
        text = re.sub("\xa0", " ", text.lower())
        if not bool(re.compile(r"shipper:").search(text)):  # for docs that start with "stop" with no shipper
            if bool(re.compile(r"stop:").search(text)):  # ...so that other functions work correctly
                text = re.sub("stop:", "shipper:                     stop:", text)
        rate_con_details = get_rate_confirmation_schema()
        rate_con_details.update({"purpose": "ORIGINAL"})
        rate_con_details.update({"sender": "WERNER LOGISTICS"})
        if ratecon_client(text):  # client
            rate_con_details.update({"client": f"{ratecon_client(text)}"})
        else:
            rate_con_details.update({"client": "WERNER LOGISTICS"})
        if ratecon_references_blob(text):  # ratecon-level references extract
            ratecon_blob = ratecon_references_blob(text)
            if references_extract(ratecon_blob):
                ratecon_ref = references_extract(ratecon_blob)
                for ref in ratecon_ref:
                    rate_con_details["references"].append(ref)
        
        if stop_blobs(text):
            pickups = stop_blobs(text)[0]
            for pick in pickups:
                stops = stop_entity_data_extract("PICK", pick)
                if stop_entity_data_extract("PICK", pick):  # stop-level entity --> ratecon-level entities extract
                    rate_con_details["entities"].append(stop_entity_data_extract("PICK", pick))
                if full_stop_data_extract("PICK", pick):
                    rate_con_details["stops"].append(full_stop_data_extract("PICK", pick))
            drops = stop_blobs(text)[1]
            for drop in drops:
                if stop_entity_data_extract("DROP", drop):  # stop-level entity --> ratecon-level entities extract
                    rate_con_details["entities"].append(stop_entity_data_extract("DROP", drop))
                if full_stop_data_extract("DROP", drop):
                    rate_con_details["stops"].append(full_stop_data_extract("DROP", drop))   
                    

        if entities_broker_blob(text):
            if entities_broker_extract(text):  # broker entity extract
                broker_ent = entities_broker_extract(text)
                rate_con_details["entities"].append(broker_ent) 
        if rate_confirmation_dates(text):  # document-level dates extract ("printed" is the same as normal doc_date)
            
            rate_con_details.update({"dates": rate_confirmation_dates(text)}) 
        if universal_notes_extract("RATECON", text):  # ratecon-level notes/comments extract
            rate_con_details["notes"].append(universal_notes_extract("RATECON", text)) 
        if ratecon_receiver(text):  # reciever extract
            rate_con_details["receiver"].update({"name": f"{ratecon_receiver(text)}"})
        if rate_confirmation_identifier(text):  # identifier extract
            rate_con_details.update({"identifier": f"{rate_confirmation_identifier(text)}"}) 
        if rate_confirmation_identifier_type(text):  # identifier_type extract
            rate_con_details.update({"identifier_type": f"{rate_confirmation_identifier_type(text)}"}) 
        if rate_confirmation_shipment_equipment_number(text):  # shipment_equipment_number extract
            rate_con_details["shipment"].update({"equipment_number": f"{rate_confirmation_shipment_equipment_number(text)}"})
        if rate_confirmation_shipment_weight(text):  # shipment_weight extract
            rate_con_details["shipment"].update({"weight": f"{rate_confirmation_shipment_weight(text)}"})
        if rate_confirmation_shipment_weight_unit_code(text):  # shipment_weight_unit_code extract
            rate_con_details["shipment"].update({"weight_unit_code": f"{rate_confirmation_shipment_weight_unit_code(text)}"})
        if rate_confirmation_shipment_volume(text):  # shipment_volume extract
            rate_con_details["shipment"].update({"volume": f"{rate_confirmation_shipment_volume(text)}"})
        if rate_confirmation_shipment_volume_qualifier(text):  # shipment_volume_qualifier extract
            rate_con_details["shipment"].update({"volume_qualifier": f"{rate_confirmation_shipment_volume_qualifier(text)}"})
        if rate_confirmation_shipment_truck_type(text):  # shipment_truck_type extract
            rate_con_details["shipment"].update({"truck_type": f"{rate_confirmation_shipment_truck_type(text)}"})
        if rate_confirmation_shipment_charges(text):  # shipment_charges extract
            rate_con_details["shipment"].update({"charges": f"{rate_confirmation_shipment_charges(text)}"})
        if rate_confirmation_shipment_loading_quantity(text):  # shipment_loading_quantity extract
            rate_con_details["shipment"].update({"loading_quantity": f"{rate_confirmation_shipment_loading_quantity(text)}"})
            

        return rate_con_details

    except Exception as e:
        print(f"[KVT-ERROR][<Werner Logistics>] \n{e}")
        rate_con_details = get_rate_confirmation_schema()
        return rate_con_details
        