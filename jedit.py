import json

class JSONDecodeError(Exception):
	pass

#{'key': {'key2': {'key3': 'value'}}}
def add(key, value, file, key2=-1, key3=-1):
    try:
        data = load(file)
        if data == {}:
            raise(KeyError)
        if not key2 == -1:
            if not key3 == -1:
                new_val = {key3:value}
                data[key][key2] = {**data[key][key2], **new_val}
            else:
                new_val = {key2:value}
                data[key] = {**data[key], **new_val}
        else:
            new_val = {key:value}
            data = {**data, **new_val}
    except(json.decoder.JSONDecodeError):
        raise JSONDecodeError
    except(KeyError):
        if not key2 == -1:
            if not key3 == -1:
                new_val = {key3:value}
                new_val = {key2:new_val}
            else:
                new_val = {key2:value}
            new_val = {key:new_val}
        else:
            new_val = {key:value}
        data = {**data, **new_val}
    finally:
        try:
            __dump(data, file)
        except(UnboundLocalError):
            pass

#{'key': {'key2': {'key3': 'value'}}}
def append(key, value, file, key2=-1):
    try:
        data = load(file)
        if not key2 == -1:
            list = data[key][key2]
        else:
            list = data[key]
        list.append(value)
        try:
            if not key2 == -1:
                data[key] = {**data[key], **{key2:list}}
        except(TypeError):
            pass
    except(KeyError):
        if not key2 == -1:
            list = [key2[value]]
        else:
            list = [value]
        data = {key:list}
    finally:
        try:
            __dump(data, file)
        except(UnboundLocalError):
            pass

#{'key': {'key2': {'key3': 'value'}}}
def edit(key, value, file, key2=-1, key3=-1):
    data = load(file)
    
    if not key2 == -1:
        if not key3 == -1:
            data[key][key2][key3] = value
        else:
            data[key][key2] = value
    else:
        data[key] = value
    __dump(data, file)

#{'key': {'key2': {'key3': 'value'}}}
def remove(key, file, key2=-1, key3=-1):
    data = load(file)

    if not key2 == -1:
        if not key3 == -1:
            del data[key][key2][key3]
        else:
            del data[key][key2]
    else:
        del data[key]
    __dump(data, file)

def load(file):
    with open(file, "r") as f:
        return(json.load(f))

def create(file):
    with open(file, "w+"):
        __dump({}, file)

def format(file):
    __dump({}, file)

def __dump(data, file):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)
