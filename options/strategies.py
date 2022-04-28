from options.option import Buy, Call, Option, Put, Sell


def condor_call(strike, spread, inner):
    return [
        Option(strike - (spread + inner), Call, Buy),
        Option(strike - inner, Call, Sell),
        Option(strike + inner, Call, Sell),
        Option(strike + (spread + inner), Call, Buy),
    ]
