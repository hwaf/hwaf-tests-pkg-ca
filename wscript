# -*- python -*-

import waflib.Logs as msg

def pkg_deps(ctx):
    ctx.use_pkg('pkg-aa')
    ctx.use_pkg('pkg-ab')
    return

def configure(ctx):
    ctx.load('find_python')
    ctx.find_python()
    return

def build(ctx):
    ctx(
        features="cxx cxxprogram",
        name="app-pkg-ca",
        source="src/pkg-ca.cxx",
        target="app-pkg-ca",
        use="ROOT pkg-aa pkg-ab",
        )

    # use task-a -> b -> cxx
    ctx(
        features="cxx cxxshlib",
        name="pkg-ca",
        source="src/ca.in",
        target="pkg-ca",
        use="ROOT pkg-aa pkg-ab",
        )

    ctx(
        features     = 'py',
        name         = 'py-pkgca',
        source       = 'python/pkgca.py',
        install_path = '${INSTALL_AREA}/python',
        )
    return

def install(ctx):
    return
