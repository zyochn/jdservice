import random
import requests
import base64
import json
from io import BytesIO
import time
import inspect
from pyDes import des, CBC, PAD_PKCS5, ECB
from urllib.parse import unquote
from proxy_sqlite import proxy_sql


def random_phone():
    list=['134','135','136','137','138','139','150','151','130','131','132','155','156','185','186','133','153','180','189']
    shou=random.choice(list)
    haoma="0123456789"
    haom=''
    haom1=[]
    for i in range (8):
        haom1.append(random.choice(haoma))
        haom = ''.join(haom1)
    return (shou+haom)


# 1003
def yanzhengma(img_url, code=1003):
    url = "http://www.bingtop.com/ocr/upload/"
    code_img = requests.get(img_url).content
    base64_img = base64.b64encode(bytes(code_img))
    params = {
        "username": 'testYanzhengma',
        "password": 'C8J44EhRKg3sQJr',
        "captchaData": base64_img,
        "captchaType": code 
    }
    res = requests.post(url, data=params)
    if res.status_code == 200:
        # print(res.text)
        ret_json = json.loads(res.text)
        if ret_json['message'] == '':
            return ret_json['data']['recognition']
    return None


def parse_qrcode_online(image_url):
    rq_img = requests.get(image_url).content
    img = Image.open(BytesIO(rq_img))
    txt_list = pyzbar.decode(img)
    for txt in txt_list:
        barcodeData = txt.data.decode("utf-8")
        print(barcodeData)

def parse_qrcode_local(content):
    img = Image.open(BytesIO(content))
    txt_list = pyzbar.decode(img)
    for txt in txt_list:
        barcodeData = txt.data.decode("utf-8")
        print(barcodeData)

def LOG_D(log):
    t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) 
    print('[+++]' + t, 'function', '[' + inspect.stack()[1][3] + ']' + ':', log)

def LOG_E(log):
    t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) 
    print('[---]' + t, 'function', '[' + inspect.stack()[1][3] + ']' + ':', log)


def xor(text):
    out = []
    for i in text:
        out.append(ord(i)^1)
    return byte2str(out)

def byte2str(b):
    text = ''
    for i in b:
        text += chr(i)
    return str(text)

AREA = ['重庆市', '上海市', '天津市', '北京市', '福建省福州市', '广东省广州市', '广东省佛山市', '浙江省金华市', '湖南省长沙市', '福建省莆田市', '山东省济南市', 
        '山东省日照市', '辽宁省大连市', '安徽省六安市', '江苏省连云港市', '四川省成都市', '陕西省西安市', '陕西省渭南市', '河南省三门峡市']
PROXY_API = {
    AREA[0]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=500000&city=500300&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[1]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=310000&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[2]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=120000&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[3]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=110000&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[4]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=350000&city=350100&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[5]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=440000&city=440100&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[6]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=440000&city=440600&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[7]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=330000&city=330700&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[8]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=430000&city=430100&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[9]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=350000&city=350300&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[10]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=370000&city=370100&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[11]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=370000&city=371100&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[12]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=210000&city=210200&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[13]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=340000&city=341500&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[14]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=320000&city=320700&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[15]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=510000&city=510100&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[16]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=610000&city=610100&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[17]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=610000&city=610500&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1',
    AREA[18]: 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=410000&city=411200&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1'
}

def getip_uncheck(area=None):
    for i in range(6):
        if area == None:
            area = AREA[random.randint(0, len(AREA)-1)]
            url = PROXY_API[area]
        else:
            url = PROXY_API[area]
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
            if '请添加白名单' in response.text:
                return None, None
            if 'false' in response.text:
                continue
            ip = response.text
            ip = ip.replace('\n', '')
            ip = ip.replace('\r', '')
            LOG_D(ip)
            return area, ip
    return None, None


def get_jd_account(ck):
    for item in ck.split(';'):
        if 'pin=' in item:
            return item.split('=')[1]
    return None

def des_decrypt(data,secretkey):
    des_obj = des(secretkey, ECB, secretkey, padmode=PAD_PKCS5)
    decodebs64data = base64.b64decode(data)
    return des_obj.decrypt(decodebs64data).decode('utf-8')

DES_KEY = '2E1ZMAF8'
def parse_card_info(en_info):
    de_info = des_decrypt(en_info, DES_KEY)
    info_json = json.loads(de_info.replace('[', '').replace(']', ''))
    return info_json['cardNo'], info_json['cardPass']

def time_2_ts(time_str):
    # 先转换为时间数组
    timeArray = time.strptime(time_str, "%Y-%m-%d%H:%M:%S")
    # 转换为时间戳
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

def get_time():
    now = int(time.time())
    #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y_%m_%d_%H_%M_%S", timeArray)
    # print(otherStyleTime)
    return otherStyleTime

def get_area(ck):
    if '&' in ck:
        area = ck.split('&')[1].replace(' ', '')
        area = unquote(area)
    elif 'upn=' in ck:
        for i in ck.split(';'):
            if 'upn=' in i:
                area = i.split('=')[1].replace(' ', '')
        area = xor(area)
        area = str(base64.b64decode(bytes(area, encoding='utf-8')), encoding='utf-8')
    return area
        

def get_ip_info(ip):
    LOG_D('获取ip省份信息:' + str(ip))
    url = 'https://api.ip138.com/ip/?ip=' + ip + '&token=71d3346f13ec3cc6d6ff468e77055ce0'
    j = requests.get(url).json()
    LOG_D(str(j))
    if j['ret'] == 'ok':
        return j['data'][1], j['data'][2]
    return None, None

def get_zhima(pro_code='', city_code=''):
    pro_code = str(pro_code)
    city_code = str(city_code)
    url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=' + pro_code + '&city=' + city_code + \
                '&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
        if '请添加白名单' in response.text:
            return None
        if 'false' in response.text:
            return None
        ip = response.text
        ip = ip.replace('\n', '')
        ip = ip.replace('\r', '')
        return ip     
    return None

def get_liuguan(pro_code='', city_code=''):
    pro_code = str(pro_code)
    city_code = str(city_code)
    url = 'http://ecs.hailiangip.com:8422/api/getIp?type=1&num=1&pid=' + pro_code + '&unbindTime=300&cid=' + city_code + \
        '&orderId=O22030913492661582939&time=1658169513&sign=3b9b01d15d03559b74ba00b0fd28df39&noDuplicate=0&dataType=1&lineSeparator=0&singleIp='
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
        if '白名单' in response.text:
            return None
        if '暂无可用IP' in response.text:
            return None
        ip = response.text
        ip = ip.replace('\n', '')
        ip = ip.replace('\r', '')
        return ip     
    return None

def getip_fensheng(pro, city):
    l = proxy_sql().search_area()
    for i in l:
        if city == '':
            break
        if city in i[3]:
            pro_code = i[2]
            city_code = i[4]           
            if i[0] == 'zhima':
                ip = get_zhima(pro_code, city_code)
                if ip != None:
                    LOG_D(i[1] + i[3] + ' 分省zhima: ' + ip)
                    return ip
            if i[0] == 'liuguan':
                ip = get_liuguan(pro_code, city_code)
                if ip != None:
                    LOG_D(i[1] + i[3] + ' 分省liuguan: ' + ip)
                    LOG_D(ip)
                    return ip
                else:
                    break
    for i in l:
        if pro in i[1]:
            pro_code = i[2]
            if i[0] == 'zhima':
                ip = get_zhima(pro_code)
                if ip != None:
                    LOG_D(i[1] + ' 分省zhima: ' + ip)
                    return ip
            if i[0] == 'liuguan':
                ip = get_liuguan(pro_code)
                if ip != None:
                    LOG_D(i[1] + ' 分省liuguan: ' + ip)
                    return ip
                else:
                    break
    LOG_D('未能获取分省ip')
    return None


def disable_ck(pin):
    url = 'http://127.0.0.1:9191/api/orderinfo/changecookiestatus'
    # url = 'http://175.178.195.147:9191/api/orderinfo/changecookiestatus'
    head = {
        'content-type': 'application/json'
    }
    data = {}
    data['ck_account'] = pin
    res = requests.post(url=url, headers=head, data=json.dumps(data))
    LOG_D(res.text)


if __name__ == '__main__':
    # parse_qrcode('https://qr.m.jd.com/show?appid=133&size=147&t=')
    data = 'BsBfLCzOTlBGoq5gIBRaumf56aJxrurFoDkYKoywLcgJIyRuRlJdmTwqqJ14MAkuJBVWoUctCi8Fq+4pXGi34VxQ2VF287irFgf1hfDcjLBlqx3jlqZ+ppGA/LSZ8fD89OtWnpDhel352bQn77KOQk2ysxtQjCRPIfYA0F9SCU943Vf5H9StfleUMylDQ6Fe'
    # print(parse_card_info(data))
    a1 = "2022-05-1023:40:00"
    # print(time_2_ts(a1))
    # pass
    # print(get_ipinfo('223.83.132.229'))
    # print(getip_uncheck())
    # get_time()
    # print(get_ip_area('36.143.103.75'))
    ip = getip_fensheng('河北', '廊坊')
    print(ip)
    