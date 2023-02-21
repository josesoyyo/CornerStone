# RateConfirmation-KVT-Training


<h2> Initial Schema Discussion Meeting </h2>

- The latest schema was discussed in the meeting was not the final schema, this meeting will give you idea about the fields that we will be extracting from the rate confirmations.
- [Zoom Meeting](https://duke-rpa-developer-contents.s3.amazonaws.com/documents/rpa/rate_confirmations/GMT20210922-180342_Recording_1920x1080.mp4)

<h2> Schema_dictionary.md </h2>

- This contains explanation about the rate confirmation schema.
- [Schema_dictionary.md](https://github.com/DUKEAILLC/Ratecon-KVT-Training-ascendTMS/blob/main/Schema_Dictionary.md)


<h2> functions/get_ratecon_Schema.py </h2>

- This py file has the different function which returns the sub-fields schema.
- Here are the list of functions:
  - get_rate_confirmation_schema,
  - get_reference_schema, 
  - get_dates_schema, 
  - get_note_schema, 
  - entity_schema, 
  - get_purchase_order_schema
  - get_stops_schema
- [get_ratecon_Schema.py](https://github.com/DUKEAILLC/Ratecon-KVT-Training-ascendTMS/blob/main/functions/get_ratecon_schema.py)


<h2> kvt_extract_ratecon_companyname.py </h2>

- This is where you will write your kvt code
- It should be inside "kvt_extract" function
- [kvt_extract_ratecon_companyname.py](https://github.com/DUKEAILLC/Ratecon-KVT-Training-ascendTMS/blob/main/kvt_extract_ratecon_companyname.py)


<h2> process_destination_ratecon_companyname.py </h2>

- This is where you will write your final mapping function
- It should be inside "map_destination" function
- [process_destination_ratecon_companyname.py](https://github.com/DUKEAILLC/Ratecon-KVT-Training-ascendTMS/blob/main/process_destination_ratecon_companyname.py)


<h2> testing_script.py </h2>

- This py file has code which will help you test your kvt code.
- [testing_script.py](https://github.com/DUKEAILLC/Ratecon-KVT-Training-ascendTMS/blob/main/testing_script.py)


# Documents and it's text data
<h3> data/raw_data </h3>

- Inside this folder you will see a JSON file with name "companyname_documents_links"
  - This json file contains the links of all the documents associate with that particular rate confirmation company.

<h3> data/text_data </h3>

- Inside this folder you will see a JSON file with name "companyname_text_data_links".
  - This json file contains the links of the JSON text files of all the documents associate with that particular confirmation company.
  


