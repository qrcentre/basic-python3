#! /usr/bin/env python3

"""
There's some weird workarounds here regarding importing modules in python3.
Modules are cached (cannot be imported twice), unless the importlib.reload
function is used. I also test the stdout instead of return values, since that's
what the average_temperature script gives us.

The testing is snapshot-style.
"""

import sys, os
sys.path.append(os.path.join(os.getcwd(), 'lib'))

import importlib, vcr

vcr = vcr.VCR(cassette_library_dir='tests/cassettes')

@vcr.use_cassette(match_on=['host'], record_mode='none')
def test_average_temperature_warm(capsys):
    # 'snapshot' style testing here
    import average_temperature
    out, _ = capsys.readouterr()
    temp_avg, temp_words, _ = out.split('\n')
    assert temp_avg == '27.046153846153842'
    assert temp_words == "It's pretty warm tonight"

@vcr.use_cassette(match_on=['host'], record_mode='none')
def test_average_temperature_cold(capsys):
    # 'snapshot' style testing here
    import average_temperature
    importlib.reload(average_temperature)
    out, _ = capsys.readouterr()
    print(out)
    temp_avg, temp_words, _ = out.split('\n')
    assert temp_avg == '26.684615384615384'
    assert temp_words == 'naise'