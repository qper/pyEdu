# import pandas
# import json
import requests

url = 'https://api-fns.ru/api/egr'
key = '<key>'


def get_egr_request_str(url, inn, key):
    return "{}?req={}&key={}".format(url, inn, key)


set_num_1 = [2465285955,245600169802,2466152267,2443030350,2401005391,2443018064,2465050449,
             2460102478,2466232152,2466240347,245505359708,2454021982,2465138527,2403006305,
             2461206374,2465329000,243600721770,2461212522,2463113069,2427000687,2411026288,
             2460096369,2466097009,2461042550,245400459127,2463057784,2454022009,2443044730,
             2460000123,2435006330,2454013815,241102000000,246606000000,2465220482,2465308546,
             2444302215,2466178956,242201237389,2431002510,240302190479,244300332943,2408005520,
             243100016530,2454026130,2463059855,2403006351,2456012694,2465062807,2466154391,
             241900000000,2466240410,2404001691,2466215830,2446030750,2466226085,2463225767,
             2464200620,246301562799,2461124530,2464210869,2466205624,241103718332,2460252096,
             246311000000,2464036804,242300047300,2450032581,2466000401,240700698568,241502420940,
             2464208845,2452043726,2407063505,2465320913,241104052180,245505703894,2410000343,
             240400046040,2466101209,2420072410,2464054271,2408003548,2433003485,246603681753,
             246600107999,2411028447,2452027361,245714958303,2465142756,240101101542,2465302505,
             2437005290,2465294318,246202740722,246512877558,2465314807,2466199547,2465170425,2455013374]


for item in set_num_1:
    request_str = get_egr_request_str(url, item, key)
    print("Going to get: {}".format(request_str))
    response = requests.get(request_str)
    with open("{}.json".format(item), 'wb') as json_file:
        json_file.write(response.content)