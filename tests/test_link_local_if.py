import mkbgp

def create_config(srcdir, exclude, prefix, defaulttemplate, templates, family,
                  fmtclass, timeout):
    pass

def test_function():
    print("running")
    mkbgp.create_config = create_config
    mkbgp.main()

if __name__ == "__main__":
    test_function()  