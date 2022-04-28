from options.option import Buy, Call, Option, Put, Sell


def test_options():
    opt = Option(200, Call, Buy, 58.45)
    assert opt.cost() == -58.45
    assert opt.payoff(250) == 50
    assert opt.payoff(150) == 0

    opt = Option(200, Call, Sell, 58.45)
    assert opt.cost() == 58.45
    assert opt.payoff(250) == -50
    assert opt.payoff(150) == 0

    opt = Option(200, Put, Buy, 58.45)
    assert opt.cost() == -58.45
    assert opt.payoff(250) == 0
    assert opt.payoff(150) == 50

    opt = Option(200, Put, Sell, 58.45)
    assert opt.cost() == 58.45
    assert opt.payoff(250) == 0
    assert opt.payoff(150) == -50
