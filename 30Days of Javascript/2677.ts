type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    let i = 0;
    let res = [];
    while (arr.length > 0 ){
        res.push(arr.splice(0,size));
    }
    return res
};

