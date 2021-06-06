# THIS FILE IS GENERATED FROM PADDLEPADDLE SETUP.PY
#
full_version    = '2.1.0'
major           = '2'
minor           = '1'
patch           = '0'
rc              = '0'
istaged         = True
commit          = '4ccd9a0a86ad550a861c954d70e28ef15741b310'
with_mkl        = 'ON'

def show():
    if istaged:
        print('full_version:', full_version)
        print('major:', major)
        print('minor:', minor)
        print('patch:', patch)
        print('rc:', rc)
    else:
        print('commit:', commit)

def mkl():
    return with_mkl
