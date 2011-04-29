#!/usr/bin/env python

# Copyright (c) 2010 Dmitry Alenichev <mitya@rockers.su>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import os
import sys
import getopt
import urllib

def usage():
    progname = os.path.basename(sys.argv[0])
    print "%s [-q] [-t title] email password" % progname
    sys.exit(1)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "qt:", ["quiet", "title="])
    except getopt.GetoptError, err:
        print str(err)
        usage()

    verbose = True
    post_title = ""

    for o, a in opts:
        if o in ("-q", "--quiet"):
            verbose = False
        elif o in ("-t", "--title"):
            post_title = a
        else:
            assert False, "unhandled option"

    if len(args) != 2:
        usage()

    login = args[0]
    password = args[1]

    post_type = "regular"
    post_body = sys.stdin.read()
    generator = "tumblr-post (https://github.com/alenichev/tumblr-post)"

    params = urllib.urlencode({ "body": post_body,
                                "type": post_type,
                                "title": post_title,
                                "email": login,
                                "password": password,
                                "generator": generator })
    result = urllib.urlopen("http://www.tumblr.com/api/write", params)

    if result:
        if verbose:
            print result.read()
        sys.exit(0)
    else:
        if verbose:
            print "Error!"
        sys.exit(2)

if __name__ == "__main__":
    main()
