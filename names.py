# -*- coding: UTF-8 -*-



def load_source_file():
    FILE="names-source.csv"

    file = open(FILE, "r")
    columns = [u"שם", u"מוצא", u"מין"]
    json = []
    first_line = True
    for line in file:
        if first_line:
            first_line = False
            continue
        line = line.strip()
        parts = line.split(",")
        record = {}
        for ii in xrange(0, len(columns)):
            name = columns[ii]
            value = parts[ii]

            record[name] = value


        json.append(record)

    file.close()
    return json

def save_json(data):
    import json
    file("names.json", "w").write(json.dumps(data))

def save_html(data):
    html = ["<html><head><meta charset=\"utf-8\"></head><body dir=\"rtl\"><table><tr>"]
    for k,v in data[0].items():
        html.append("<th>%s</th>" % k)
    html.append("</tr>")

    for record in data:
        html.append("<tr>")
        for k,v in record.items():
            html.append("<td>%s</td>" % v.decode("utf-8"))
        html.append("<tr/>")
    html.append("</table></body></html>")
    html = "".join(html)
    file("names.html", "w").write(html.encode("utf-8"))

data = load_source_file()
save_json(data)
save_html(data)
