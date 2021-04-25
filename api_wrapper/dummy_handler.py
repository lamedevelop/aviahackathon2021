import json


class DummyHandler:

    @staticmethod
    def getDummyData():
        return json.loads('''
[
{
	 "except_days": "",
	 "arrival": "10:00",
     "uid": "SU-1536_210430_c26_12",
     "title": "Москва — Томск",
     "number": "SU 1536",
     "short_title": "Москва — Томск",
     "carrier": {"code": 26, "codes": {"icao": "AFL", "sirena": "СУ", "iata": "SU"}, "title": "Аэрофлот"},
     "transport_type": "plane",
     "vehicle": "Boeing 737-800",
     "transport_subtype": {"color": "", "code": "", "title": ""},
     "express_type": "",
	 "is_fuzzy": "",
	 "departure": "02:00",
	 "stops": "",
	 "days": "ежедневно с 30.04 по 27.09",
	 "terminal": "B",
	 "platform": "105"
},
{
	 "except_days": "",
	 "arrival": "12:30",
     "uid": "SU-2000_222222_c22_33",
     "title": "Москва — Самара",
     "number": "SU 1536",
     "short_title": "Москва — Самара",
     "carrier": {"code": 26, "codes": {"icao": "AFL", "sirena": "СУ", "iata": "SU"}, "title": "КузьмаЭирлайнс"},
     "transport_type": "plane",
     "vehicle": "Boeing 737-800",
     "transport_subtype": {"color": "", "code": "", "title": ""},
     "express_type": "",
	 "is_fuzzy": "",
	 "departure": "04:00",
	 "stops": "",
	 "days": "ежедневно с 28.04 по 25.08",
	 "terminal": "B",
	 "platform": "106"
}
]
''')
