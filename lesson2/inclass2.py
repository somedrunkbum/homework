import urllib2, json


def get_currency_rate(currency_list):

    data = {}

    if not currency_list:
        return data

    c = ','.join(currency_list)
    u = urllib2.urlopen("https://query.yahooapis.com/v1/public/yql?"
                        "q=select+*+from+yahoo.finance.xchange+where"
                        "+pair+=+%22" + c + "%22&format=json&env=store"
                        "%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=")
    parsed_data = json.loads(u.read())

    if len(currency_list) == 1:
        data[parsed_data["query"]["results"]["rate"]["id"]] = parsed_data["query"]["results"]["rate"]["Rate"]
    else:
        for n in parsed_data["query"]["results"]["rate"]:
            data.update({str(n["id"]): n["Rate"]})

    return data


print(get_currency_rate(["EURBYR", "USDBYR", "USDRUB"]))
