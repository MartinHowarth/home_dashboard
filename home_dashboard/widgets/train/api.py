from nredarwin import webservice


def get_station_board(station_code, nre_api_key) -> webservice.StationBoard:
    darwin_sesh = webservice.DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx",
                                              api_key=nre_api_key)
    return darwin_sesh.get_station_board(station_code)
