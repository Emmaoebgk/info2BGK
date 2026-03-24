def parse_key_value_string(text, delimiter= ":", pair_separator=";"):
    result = {}
    key_values = text.split(pair_separator)
    for key_value in key_values:
        parsed = key_value.split(delimiter)
        if len(parsed) != 2:
            raise ValueError("Invalid format")
        key = parsed[0].strip()
        value = parsed[1].strip()
        result[key] = value
    return result
if __name__ == "__main__":
    parsed = parse_key_value_string(
        "name:Alice; age:30; city:London",
        delimiter=":",
        pair_separator=";"
    )
    print(parsed)