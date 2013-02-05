from optparse import OptionParser
from encoder import encode, decode

if __name__ == "__main__":
    parser = OptionParser()
    parser.set_defaults(encoder=-1, debug=False)
    parser.add_option("-f", "--file", type="string", dest="filename",
                      help="FILE to encode or decode", metavar="FILE")
    parser.add_option("-e", "--encode", action="store_true", dest="encoder",
                      help="Encode plain text file")
    parser.add_option("-d", "--decode", action="store_false", dest="encoder",
                      help="Decode previously encoded file")
    parser.add_option("-p", "--password", type="string", dest="password",
                      help="Password to encode / decode")
    parser.add_option("-t", "--test", action="store_true", dest="debug")

    (options, args) = parser.parse_args()
    if options.debug:
        # verify basic functionality
        teststring = "The quick brown fox jumped over the lazy dog"
        testpwd = "password"
        encoded = encode(teststring,testpwd)
        assert(teststring != encode(teststring,testpwd))
        assert(testpwd != encode(teststring,testpwd))
        assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
        assert(teststring == decode(encoded,testpwd))
        # try increasingly difficult strings
        teststring = "Adding numbers 12345"
        assert(teststring == decode(encode(teststring,"password"),"password"))
        teststring = "Adding special chars @#$(*^,;'"
        assert(teststring == decode(encode(teststring,"password"),"password"))
        teststring = 'with double quotes"'
        assert(teststring == decode(encode(teststring,"password"),"password"))
        print "Success!"
        exit(0)

    if not options.password:
        parser.error("You must provide a password.")
    if not options.filename:
        parser.error("You must provide a file to encode or decode")
    if options.encoder == -1:
        parser.error("You must specify whether you want to encode or decode")

    try:
        f = open(options.filename, 'r')
    except IOError:
        print "Unable to open file %s." % options.filename
    else:
        fn_pcs = options.filename.split(".")
        fn_type = fn_pcs.pop()
        if options.encoder:
            new_file = ".".join(fn_pcs) + "_e" + "." + fn_type
            try:
                fn = open(new_file, 'w')
            except IOError:
                print "Unable to open file %s." % new_file
            else:
                fn.write(encode(f.read(),options.password))
                fn.close()
        else:
            fn_pcs2 = ".".join(fn_pcs).split("_")
            if fn_pcs2[-1] == 'e':
                fn_pcs2.pop()
            new_file = "_".join(fn_pcs2) + '.' + fn_type
            try:
                fn = open(new_file, 'w')
            except IOError:
                print "Unable to open file %s." % new_file
            else:
                fn.write(decode(f.read(),options.password))
                fn.close()        
