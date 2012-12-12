# -*- python -*-

import waflib.Logs as msg

def pkg_deps(ctx):
    ctx.use_pkg('pkg-aa')
    ctx.use_pkg('pkg-ab')
    return

def configure(ctx):
    return

def build(ctx):
    ctx(
        features="cxx cxxprogram",
        name="pkg-ca",
        source="src/pkg-ca.cxx",
        target="pkg-ca",
        use="ROOT pkg-aa pkg-ab",
        )

    return

def install(ctx):
    return
