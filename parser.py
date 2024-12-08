def parse(tokens):
    html = "<html>\n  <head>\n"
    body = "  <body>\n"

    for token in tokens:
        key, value = token
        if key == "title":
            html += f"    <title>{value}</title>\n"
        elif key == "header":
            body += f"    <h1>{value}</h1>\n"
        elif key == "paragraph":
            body += f"    <p>{value}</p>\n"
        elif key == "button":
            text, link = value.split('->')
            body += f"    <button onclick=\"location.href='{link.strip()}'\">{text.strip()}</button>\n"

    html += "  </head>\n" + body + "  </body>\n</html>\n"
    return html
