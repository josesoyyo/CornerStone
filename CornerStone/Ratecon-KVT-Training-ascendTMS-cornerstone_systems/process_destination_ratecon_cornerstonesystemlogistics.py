def map_destination(kvt):
    try:
        # todo
        success = True
        return kvt, success
    except Exception as e:
        print(f"[MAPPING-ERROR][<COMPANY NAME>] \n{e}")
        success = False
        return {}, success
