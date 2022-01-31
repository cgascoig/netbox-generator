#!/usr/bin/env python3

import pynetbox
import jinja2
from os import path
import os
import logging

def main():
    url = os.getenv("NETBOX_URL")
    token = os.getenv("NETBOX_TOKEN")
    if url is None or token is None:
        logging.fatal("NETBOX_URL or NETBOX_TOKEN not set")

    template_path=os.getenv("NETBOX_TEMPLATE_PATH", "templates")
    output_path=os.getenv("NETBOX_OUTPUT_PATH", ".")
        
    nb = pynetbox.api(url, token=token)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path), autoescape=False)

    for template_name in env.list_templates(["j2"]):
        print(f"Processing template {template_name}")
        t = env.get_template(template_name)
        t.stream(netbox=nb).dump(path.join(output_path, path.splitext(template_name)[0]))


if __name__ == "__main__":
    main()