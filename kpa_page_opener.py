#!/usr/bin/env python3
"""KPA1500 page opener - runs on the computer that runs Thetis when the bridge runs on ANOTHER computer.

A Thetis HELP / SETTINGS / APPLET button reaches the bridge, and the bridge sends a short message here.
This program then opens that page of the bridge in this computer's browser.

Safety: it listens only for messages from the bridge's own address, understands only the three words
KPA_OPEN_HELP, KPA_OPEN_PANEL and KPA_OPEN_APPLET, and can only open the bridge's own pages
(http://BRIDGE:PORT/help, /, /applet). It never starts anything else.

  python kpa_page_opener.py --bridge 192.168.1.60 [--web-port 8080] [--listen-port 50103]

Design by KW4EX. MIT license. No warranty.
"""
import argparse
import socket
import sys
import time
import webbrowser

PAGES = {"KPA_OPEN_HELP": "/help", "KPA_OPEN_PANEL": "/", "KPA_OPEN_APPLET": "/applet"}


def page_url(token, bridge, web_port):
    """the one page a message asks for, or None for anything else"""
    path = PAGES.get(str(token).strip().upper())
    return None if path is None else "http://%s:%d%s" % (bridge, int(web_port), path)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Opens the bridge's pages here when a Thetis button asks for them")
    ap.add_argument("--bridge", required=True, help="IP address of the computer running the bridge")
    ap.add_argument("--web-port", type=int, default=8080, help="the bridge's web port (default 8080)")
    ap.add_argument("--listen-port", type=int, default=50103, help="UDP port to listen on (default 50103)")
    a = ap.parse_args(argv)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind(("0.0.0.0", a.listen_port))
    except OSError as e:
        print("Cannot listen on UDP port %d (%s). Is another page opener already running?" % (a.listen_port, e))
        return 1
    print("KPA1500 page opener: waiting for the bridge at %s (UDP %d). Close this window to stop." % (a.bridge, a.listen_port))
    last = 0.0
    while True:
        try:
            data, addr = sock.recvfrom(256)
        except OSError:
            time.sleep(0.5)
            continue
        if addr[0] != a.bridge:
            continue                                  # only the bridge may ask
        url = page_url(data.decode("ascii", "replace"), a.bridge, a.web_port)
        if url and time.time() - last > 0.5:          # ignore double sends
            last = time.time()
            print("Opening %s" % url)
            try:
                webbrowser.open(url)
            except Exception as e:
                print("Could not open the browser: %s" % e)


if __name__ == "__main__":
    sys.exit(main())
