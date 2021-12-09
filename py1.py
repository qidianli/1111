import kopl

from kopl.test.test_example import *

run_test()

engine.QueryAttr(
    engine.Find("1985 Major League Baseball season"),
    "point in time"
)