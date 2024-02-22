from src import select_time

time_select = [{"date": "2019-08-26T10:50:58.294041"}, {"date": "2019-07-03T18:35:29.512364"},
               {"date": "2018-06-30T02:08:58.425572"}, {"date": "2018-03-23T10:45:06.972075"},
               {"date": "2019-04-04T23:20:05.206878"}, {"date": "2019-03-23T01:09:46.296404"}]

def test_select_time():
    assert select_time.select_last(time_select) == [{"date": "2019-08-26 10:50:58.294041"},
                                         {"date": "2019-07-03 18:35:29.512364"},
                                         {"date": "2019-04-04 23:20:05.206878"},
                                         {"date": "2019-03-23 01:09:46.296404"},
                                         {"date": "2018-06-30 02:08:58.425572"}]
    assert len(select_time.select_last(time_select)) == 5

